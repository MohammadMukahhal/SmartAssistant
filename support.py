import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Func to clean question and generate search query
def CleanQuestion(question:str):
    # # Getting stop words dataset
    # nltk.download('stopwords')
    # stop_words = set(stopwords.words('english'))
    # additional_excluded_words = {'?', 'years?'} 
    # excluded_words = stop_words.union(additional_excluded_words)
    # keywords = question.split()
    # keywords = [word for word in keywords if word.lower() not in excluded_words]
    # search_query = ' '.join(keywords)
    # print("SEARCHED FOR: ",search_query)
    # return search_query

    # Tokenize the text into words
    tokens = word_tokenize(question)
    
    # Convert tokens to lowercase
    tokens = [word.lower() for word in tokens]
    
    # Remove punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [word.translate(table) for word in tokens]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [word for word in stripped if word not in stop_words]
    
    # Join tokens to form a cleaned sentence
    cleaned_text = ' '.join(cleaned_tokens)
    
    return cleaned_text

CleanQuestion("What is one of the significant contributions to the field of artificial intelligence in recent years?")