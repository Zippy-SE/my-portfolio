print(" -- Contact Book Application -- ")

contacts = {}

while True:
    print("\nOptions:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        if not contacts:
            print("No contacts in the book.")
        else:
            print("Your Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == '2':
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        contacts[name] = phone
        print(f'Contact "{name}" added.')
    elif choice == '3':
        if not contacts:
            print("No contacts to search.")
        search_name = input("Enter the contact name to search: ")
        if search_name in contacts:
            print(f'Found contact - {search_name}: {contacts[search_name]}')
    elif choice == '4':
        if not contacts:
            print("No contacts in book.")
        else:
            print("Your contacts:")
        for i, (name, phone) in enumerate(contacts.items(), 1):
            print(f"{i}. {name}: {phone}")
        itemno = input("Enter the number of the contact to remove: ")
        if itemno.isdigit():
            idx = int(itemno) - 1
            if 0 <= idx < len(contacts):
                name_to_remove = list(contacts.keys())[idx]
                del contacts[name_to_remove]
                print(f'Contact "{name_to_remove}" removed.')
            else:
                print("Invalid contact number.")
        else:
            print("Please enter a valid number.")
    elif choice == '5':
        print("Exiting Contact Book Application. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 4.")