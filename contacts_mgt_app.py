# This manages your contacts using Python.

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Show All Contacts")
    print("6. Exit")

def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            contacts[name] = number
            print(f"Contact '{name}' added.")

        elif choice == "2":
            name = input("Enter contact name to update: ")
            if name in contacts:
                number = input("Enter new phone number: ")
                contacts[name] = number
                print(f"Contact '{name}' updated.")
            else:
                print("Contact not found.")

        elif choice == "3":
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Contact not found.")

        elif choice == "4":
            name = input("Enter contact name to search: ")
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print("Contact not found.")

        elif choice == "5":
            if contacts:
                print("\n--- All Contacts ---")
                for name, number in contacts.items():
                    print(f"{name}: {number}")
            else:
                print("No contacts found.")

        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
