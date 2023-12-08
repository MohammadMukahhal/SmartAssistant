import wikipedia

def WikiQuery(query):
    print("input query: ",query)
    search_result = wikipedia.search(query)
    print(search_result)
    try:
        summary = wikipedia.summary(search_result[0], sentences=4, auto_suggest=False, redirect=True)
        print(summary)
        return summary
    except:
        return "Page not found."
