from feature-3 import search
from content_management_features import main_contacts
# import 

def open_menu():
  print("""
         _.._           
     __.--"" __ ""--.__    
   .'//   .-"  "-.   \\`,  
  : :'  .'.  :;  ,`.  `; ; 
 /; ;  /  T. $$ ,P  \  : : 
/: :  ;    T.:;,P    :  ; ;
)| | :      `  '      ; | |
`j | :.--------------.: | |
 ; ; |                | : :
 ; ; |                | : :
 | | |                | | |
 | | |                | | |
 : : |                | ; ;
 : : :________________: ; ;
  ; ;__    _...._    __: : 
  | ;  "-./ ,--, \,-"  : | 
  | '._   \ ;  : /   _.' | 
  :  __`-. `."",' .-'__  ; 
   ;`.__> `.J__L.' <__.':  
   ;.--._   .--.   _.--,:  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   ;`.__.' `.__.' `.__.':  
  : .--._   .--.   _.--, ; 
  ; `.__.' `.__.' `.__.' : 
  ;                      : 
  '--..__          __..--'
""")
  print("""
  Menu:
        
    Type 1 to Contacts
    Type 2 to Search
    Type 3 to Manage Tasks
        """)
  select_menu = input("Type a number to choose menu: ")
  # num_selected = int(select_menu)
  if select_menu == "1":
    return main_contacts()
  elif select_menu == "2":
    return search()
  elif select_menu == "3":
    print("Manage Tasks go here.")
  else:
    print("Pick only 1-3 number, try again!")


  
open_menu()