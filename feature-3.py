from menu import open_menu
import webbrowser

prior_searches = []  

def search():
    search_term = input('What do you want to search?')
    prior_searches.append(search_term)
    print(prior_searches)
    webbrowser.open(f'https://www.google.com/search?q={search_term}')
    yes_no = input('Would you like to search again Y/N?').upper()
    while yes_no != 'Y' or yes_no != 'N':
        yes_no = input('Would you like to search again Y/N?').upper()

    if yes_no == 'Y':
        search()
    else:
        open_menu()
