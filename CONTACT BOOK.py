import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts in the contact book."""
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print()

def delete_contact(contacts):
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
