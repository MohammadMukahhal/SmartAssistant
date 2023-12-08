import torch
from transformers import BertForQuestionAnswering, BertTokenizer
import warnings
warnings.simplefilter("ignore")

def processNLP(question:str, context:str):

    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    
    input_ids = tokenizer.encode(question, context,max_length=512, truncation=True)
    print("The input has a total of {} tokens.".format(len(input_ids)))
    tokens = tokenizer.convert_ids_to_tokens(input_ids)
        
    sep_idx = input_ids.index(tokenizer.sep_token_id)
    num_seg_a = sep_idx+1
    num_seg_b = len(input_ids) - num_seg_a
    segment_ids = [0]*num_seg_a + [1]*num_seg_b#making sure that every input token has a segment id
    assert len(segment_ids) == len(input_ids)
    
    #token input_ids to represent the input and token segment_ids to differentiate our segments - question and text
    output = model(torch.tensor([input_ids]),  token_type_ids=torch.tensor([segment_ids]))
    
    #tokens with highest start and end scores
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)
    if answer_end >= answer_start:
        answer = " ".join(tokens[answer_start:answer_end+1])
    else:
        print("I am unable to find the answer to this question. Can you please ask another question?")
        
    print("\nQuestion:\n{}".format(question.capitalize()))
    print("\nAnswer:\n{}.".format(answer.capitalize()))
    return answer

    #del model
    #del tokenizer
