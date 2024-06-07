from main import open_menu()

#empty list for contact storage
# contacts = []

#CRUD
##create new contact dictionary
def create_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contact = {
        "name": name,
        "phone": phone
    } #dict
    contacts.append(contact)
    print("Contact added.")
    main()

##read contact
def read_contact():
    if len(contacts) == 0:
        print("Contacts empty.")
    else:
        for i in range(len(contacts)):
            contact = contacts[i]
            print(str(i + 1) + ". Name: " + contact["name"] + ", Phone: " + contact["phone"])
    main()

##update contact
def update_contact():
    index = int(input("Enter contact index to update: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Invalid contact index.")
        return

    name = input("Enter new name: ")
    phone = input("Enter new phone: ")

    contacts[index]["name"] = name
    contacts[index]["phone"] = phone
    print("Contact updated.")
    main()5


##delete contact
def delete_contact():
    if len(contacts) == 0:
        print("No contacts to delete.")
        return

    index = int(input("Enter index number to delete: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Invalid contact number.")
    else:
        del contacts[index]
        print("Contact deleted.")
    main()



#MAIN MENU

##main menu function
def main_contacts():
    while True:
        print("Select an option:")
        print("Type 1 to create")
        print("Type 2 to read")
        print("Type 3 to update")
        print("Type 4 to delete")
        print("Type 5 to exit")
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
