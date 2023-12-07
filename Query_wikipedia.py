import wikipediaapi

def WikiQuery(query):
    print("input query: ",query)
    wiki_wiki = wikipediaapi.Wikipedia('My Project','en')
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "Page not found."
