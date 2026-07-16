
name = input("What is your name?: ")
phone = input("What is your cellphone number?: ")
email = input("What is your email address?: ")






def add_contact (contacts, name, phone, email,):
    new_contact= {
        "name": name,
        "phone": phone,
        "email" : email
    }
    contacts.append(new_contact)
    print(f"Contact {name} has been added.")

contacts = []
add_contact(contacts, name, phone, email)
print(contacts)
