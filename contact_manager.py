import json
import re

# Data storage: Dictionary to hold contacts
contacts = {}

def display_welcome_message():
    """Display the welcome message."""
    print("Welcome to the Contact Management System!")

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    """Add a new contact to the dictionary."""
    try:
        identifier = input("Enter a unique identifier (phone/email): ").strip()
        if identifier in contacts:
            raise ValueError("Contact already exists.")
        
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        address = input("Enter address (optional): ").strip()
        notes = input("Enter notes (optional): ").strip()

        # Validate email and phone
        if not re.match(r"^[\w\.-]+@[\w\.-]+$", email):
            raise ValueError("Invalid email format.")
        if not re.match(r"^\d{10}$", phone):
            raise ValueError("Phone number must be 10 digits.")

        contacts[identifier] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "notes": notes
        }
        print("Contact added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def edit_contact():
    """Edit an existing contact."""
    try:
        identifier = input("Enter the unique identifier of the contact to edit: ").strip()
        if identifier not in contacts:
            raise ValueError("Contact not found.")
        
        print("Leave fields empty if you don't want to change them.")
        name = input(f"Enter new name (current: {contacts[identifier]['name']}): ").strip()
        phone = input(f"Enter new phone number (current: {contacts[identifier]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[identifier]['email']}): ").strip()
        address = input(f"Enter new address (current: {contacts[identifier]['address']}): ").strip()
        notes = input(f"Enter new notes (current: {contacts[identifier]['notes']}): ").strip()

        # Validate email and phone if provided
        if email and not re.match(r"^[\w\.-]+@[\w\.-]+$", email):
            raise ValueError("Invalid email format.")
        if phone and not re.match(r"^\d{10}$", phone):
            raise ValueError("Phone number must be 10 digits.")

        if name:
            contacts[identifier]['name'] = name
        if phone:
            contacts[identifier]['phone'] = phone
        if email:
            contacts[identifier]['email'] = email
        if address:
            contacts[identifier]['address'] = address
        if notes:
            contacts[identifier]['notes'] = notes
        
        print("Contact updated successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_contact():
    """Delete a contact by its identifier."""
    try:
        identifier = input("Enter the unique identifier of the contact to delete: ").strip()
        if identifier not in contacts:
            raise ValueError("Contact not found.")
        
        del contacts[identifier]
        print("Contact deleted successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def search_contact():
    """Search for a contact by its identifier."""
    try:
        identifier = input("Enter the unique identifier of the contact to search: ").strip()
        if identifier not in contacts:
            raise ValueError("Contact not found.")
        
        contact = contacts[identifier]
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")
    except ValueError as e:
        print(f"Error: {e}")

def display_all_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        for identifier, contact in contacts.items():
            print(f"\nIdentifier: {identifier}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print(f"Notes: {contact['notes']}")

def export_contacts():
    """Export contacts to a text file."""
    try:
        filename = input("Enter the filename to export contacts to: ").strip()
        with open(filename, 'w') as file:
            for identifier, contact in contacts.items():
                file.write(f"Identifier: {identifier}\n")
                file.write(f"Name: {contact['name']}\n")
                file.write(f"Phone: {contact['phone']}\n")
                file.write(f"Email: {contact['email']}\n")
                file.write(f"Address: {contact['address']}\n")
                file.write(f"Notes: {contact['notes']}\n\n")
        print("Contacts exported successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def import_contacts():
    """Import contacts from a text file."""
    try:
        filename = input("Enter the filename to import contacts from: ").strip()
        with open(filename, 'r') as file:
            data = file.read().strip().split('\n\n')
            for entry in data:
                lines = entry.split('\n')
                if len(lines) < 6:
                    continue
                
                identifier = lines[0].split(': ')[1]
                contacts[identifier] = {
                    "name": lines[1].split(': ')[1],
                    "phone": lines[2].split(': ')[1],
                    "email": lines[3].split(': ')[1],
                    "address": lines[4].split(': ')[1],
                    "notes": lines[5].split(': ')[1]
                }
        print("Contacts imported successfully.")
    except IOError as e:
        print(f"Error reading from file: {e}")

def main():
    """Main function to run the Contact Management System."""
    display_welcome_message()
    
    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                edit_contact()
            elif choice == 3:
                delete_contact()
            elif choice == 4:
                search_contact()
            elif choice == 5:
                display_all_contacts()
            elif choice == 6:
                export_contacts()
            elif choice == 7:
                import_contacts()
            elif choice == 8:
                print("Quitting the application.")
                break
            else:
                raise ValueError("Invalid option. Please select a number between 1 and 8.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
