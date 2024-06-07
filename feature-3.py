import webbrowser

prior_searches = []

def internet():
    search_term = input('What do you want to search?')
    prior_searches.append(search_term)
    webbrowser.open(f'https://www.google.com/search?q={search_term}')

def history():
    print(prior_searches)
