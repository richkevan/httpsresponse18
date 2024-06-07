import webbrowser

#prior_searches = []  

def search():
    search_term = input('What do you want to search?')
    prior_searches.append(search_term)
    print(prior_searches)
    webbrowser.open(f'https://www.google.com/search?q={search_term}')
    any_key = input('Hit any key to return to menu...')
    if any_key:
        open_menu()