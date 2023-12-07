def fetch_wikipedia_summary(query: str):
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "No Wikipedia page found for this query."
