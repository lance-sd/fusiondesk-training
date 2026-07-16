# ==== Contact Book ====
import json
# Add contact
contacts = []

def add_contact (contacts, name, phone, email):
    new_contact= {
        "name": name,
        "phone": phone,
        "email" : email
    }
    contacts.append(new_contact)
    print(f"Contact {name} has been added.")



# List contacts

def list_contacts (contacts):
    if len(contacts) == 0:
        print("No contacts saved.")
        return
    
    print(f"You have {len(contacts)} contact(s)")

    for contact in contacts:
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("=" * 30)


#  Search contacts

def search_contacts(contacts, search_term):
    results = []    

    for contact in contacts:
        if search_term.lower() in contact["name"].lower():
            results.append(contact)
    return results


# Delete contact
def delete_contact(contacts, to_delete):
    for index, contact in enumerate(contacts):
        if contact["name"].lower() == to_delete.lower():
            contacts.pop(index)
            print(f"Contact {to_delete} has been delted.")
            return
        
    print(f"No contact name {to_delete} was found.")



def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
    
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)





def main():
    print("*****Contact Book*****")
    contacts = load_contacts()

    while True:
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contacts")
        print("4. Delete contacts")
        print("5. Quit")

        choice = input("What would you like to do?(Choose between 1-5): ")

        if choice == "1":
            name = input("Name of new contact?: ")
            phone = input("Phone of new contact?: ")
            email = input("Email of new contact?: ")
            add_contact(contacts, name, phone, email)
            save_contacts(contacts)

        elif choice == "2":
            list_contacts(contacts)

        elif choice == "3":
            search_term = input("Search contact by name: ")
            results = search_contacts(contacts, search_term)
            if len(results) == 0:
                print("No contacts found")
            else:
                for contact in results:
                    print(f"name: {contact['name']}")
                    print(f"phone: {contact['phone']}")
                    print(f"email: {contact['email']}")

        elif choice == "4":
            to_delete = input("name of contact to delete: ")
            delete_contact(contacts, name)
            save_contacts(contacts)

        elif choice == "5":
            print("thank you...goodbye!!")
            break

        else:
            print("Invalid option, please pick a number between 1 & 5")

if __name__ == "__main__":
    main()




