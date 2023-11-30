import nltk
from nltk.corpus import stopwords

#Func to clean question and generate search query
def CleanQuestion(question:str):
    # Getting stop words dataset
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    additional_excluded_words = {'?', 'years?'} 
    excluded_words = stop_words.union(additional_excluded_words)
    keywords = question.split()
    keywords = [word for word in keywords if word.lower() not in excluded_words]
    search_query = ' '.join(keywords)
    print("SEARCHED FOR: ",search_query)
    return search_query

CleanQuestion("What is one of the significant contributions to the field of artificial intelligence in recent years?")