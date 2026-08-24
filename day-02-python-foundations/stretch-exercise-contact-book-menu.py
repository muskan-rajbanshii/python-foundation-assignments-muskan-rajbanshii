
contacts = {
    "contact1" : {
        "Name" : "Ram",
        "Phone_number" : 9835621354,
        "Email_address" : "ram2@gmail.com"
    },
    "contact2": {
        "Name" : "Sita",
        "Phone_number" : 9835621353,
        "Email_address" : "sita5@gmail.com"
     },
     "contact3" : {
        "Name" : "Rita",
        "Phone_number" : 9804398321,
        "Email_address" : "rita8@gmail.com"
     }
 }


choice = 0
while choice != 5:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")


    ##Add contact
    choice =  int(input("Enter your choice : "))
    if choice == 1 :
        # print(f"contact{len(contacts)+1}")
        contacts[f"contact{len(contacts)+1}"] = {
            "Name" : input("Enter name: ").title(),
            "Phone_number" : input("Enter your phone number: "),
            "Email_address" : input("Enter your email: ")
    }
        print("Contact added successfully.") 

    ##search contact
    elif choice == 2:
        found = False
        name = input("Enter the name of the contact : ").title()
        for key,value in contacts.items():
            if name ==  value["Name"]:
                print("Found")
                found = True
                break
        if found == False:
            print(f"{name} is not availabe in contact list.")
            
    #delete contact
    elif choice == 3:
        name = input("Enter the name you want to delete: ").title()
        delete_key = None
        for key,value in contacts.items():
            if name == value["Name"]:
                delete_key = key
                break
        if delete_key is not None:
            del  contacts[delete_key]
            print("Contact deleted.")
        else:
            print("Contact not found")


    #Display all contact
    elif  choice == 4:
        print("All Contacts: ")
        for key,value in contacts.items():
            print(f"{key} = {value}")

    #exit
    elif choice == 5:
        print("ThANKOU FOR USING IT.")
        break

    else:
        print("Invalid choice. Try again")
