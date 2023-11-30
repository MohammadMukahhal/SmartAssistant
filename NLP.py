import torch
from transformers import BertForQuestionAnswering, BertTokenizer
import warnings
warnings.simplefilter("ignore")

def processNLP(question:str, context:str):

    weight_path = "bert-large-uncased-whole-word-masking-finetuned-squad"

    tokenizer = BertTokenizer.from_pretrained(weight_path)
    model = BertForQuestionAnswering.from_pretrained(weight_path)

    #question = "What is one of the significant contributions to the field of artificial intelligence in recent years?"
    #context = "In recent years, deep learning has gained immense popularity in the field of artificial intelligence. One of the pivotal developments in this domain was the introduction of transformer-based models like BERT (Bidirectional Encoder Representations from Transformers). These models have demonstrated exceptional performance across various natural language processing tasks, including text classification, named entity recognition, question answering, and more."

    input_ids = tokenizer.encode(question, context)

    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    sep_idx = tokens.index('[SEP]')

    token_type_ids = [0 for i in range(sep_idx+1)] + [1 for i in range(sep_idx+1,len(tokens))]

    out = model(torch.tensor([input_ids]), 
                    token_type_ids=torch.tensor([token_type_ids]))

    start_logits, end_logits = out['start_logits'], out['end_logits']

    max_answer_len = 5  # Change this value to control the number of words in the answer

    answer_start = torch.argmax(start_logits)
    answer_end = torch.argmax(end_logits)

    # Generating a longer answer by considering a range around the max probabilities
    start_idx = max(0, answer_start - max_answer_len // 2)
    end_idx = min(len(tokens), answer_end + max_answer_len // 2)

    ans = ' '.join(tokens[start_idx:end_idx])
    print('Predicted answer:', ans)
    return ans

    #del model
    #del tokenizer
