from main import open_menu()

#empty list for contact storage
contacts = []

#CRUD
##create new contact dictionary
def create_contact():
    name = input("Enter name: ") #input name
    phone = input("Enter phone: ") #input phone
    contact = {
        "name": name,
        "phone": phone
    } #dict save
    contacts.append(contact) #appends to contacts list
    print("Contact added.")
    main_contacts() #noticed it runs menu twice need ot figure out why

##read contact
def read_contact():
    if len(contacts) == 0: #equals no contacts
        print("Contacts empty.")
    else:
        for i in range(len(contacts)): #iterates through contacts position 0 thorugh len of list
            contact = contacts[i]
            print(str(i + 1) + ". Name: " + contact["name"] + ", Phone: " + contact["phone"]) #this print could be cleaner I think
    main_contacts() #noticed it runs menu twice need ot figure out why

##update contact
def update_contact():
    index = int(input("Enter contact index to update: ")) - 1 #user needs to input index nr
    if index < 0 or index >= len(contacts): #won't work if index less than 0 or max entry index num
        print("Invalid contact index.")
        return

    ##code bit was taken from medium article regarding CRUD
    ##suggests turning into ints and ensuring there's an invalid choice.

    name = input("Enter new name: ")
    phone = input("Enter new phone: ")

    contacts[index]["name"] = name #replaces value of name at index num
    contacts[index]["phone"] = phone #replaces value of phone at index num
    print("Contact updated.")
    main_contacts() #noticed it runs menu twice need ot figure out why


##delete contact
def delete_contact():
    if len(contacts) == 0: #equals no contacts
        print("No contacts to delete.")
        return

    index = int(input("Enter index number to delete: ")) - 1 #same as update
    if index < 0 or index >= len(contacts): 
        print("Invalid contact number.")
    ##code bit was taken from medium article regarding CRUD
    ##suggests turning into ints and ensuring there's an invalid choice.
    
    else:
        del contacts[index]
        print("Contact deleted.")
    main_contacts() #noticed it runs menu twice need ot figure out why


#MAIN MENU

##main menu function
def main_contacts():
    print("""
    Select an option:
    
    Type 1 to create.
    Type 2 to read.
    Type 3 to update.
    Type 4 to delete.
    Type 5 to exit.
    """)

    ##totally stole the format from menu.py because I was printing each file before
    
    choice = input("Please enter your choice: ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        read_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        open_menu()
    else:
        print("Invalid choice. Please try again.")

