class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {contact_name} updated successfully!")
                return
        print(f"Contact {contact_name} not found.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact_name} deleted successfully!")
                return
        print(f"Contact {contact_name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("-----------------------")
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book")
            break

        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
