import webbrowser

#prior_searches = []  

def search():
    search_term = input('What do you want to search?')
    prior_searches.append(search_term)
    print(prior_searches)
    webbrowser.open(f'https://www.google.com/search?q={search_term}')

