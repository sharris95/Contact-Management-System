#ContactManagementSystem App

import re
import csv
import os

def load_contacts():
    contacts = {}
    if os.path.exists("contacts.csv"):
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                unique_id = row['unique_id']
                contacts[unique_id] = row
    return contacts

def save_contacts(contacts):
    with open("contacts.csv", "w", newline='') as file:
        fieldnames = ['unique_id', 'name', 'phone', 'email', 'additional_info']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for unique_id, details in contacts.items():
            row = {'unique_id': unique_id}
            row.update(details)
            writer.writerow(row)

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return re.match(r"\d{10}", phone)

def add_contact(contacts):
    unique_id = input("Enter unique identifier (phone or email): ").strip()
    if unique_id in contacts:
        print("Contact already exists.")
        return
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    additional_info = input("Enter additional information: ").strip()

    if not validate_email(email):
        print("Invalid email format.")
        return
    if not validate_phone(phone):
        print("Invalid phone format. Use 10 digits.")
        return

    contacts[unique_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "additional_info": additional_info
    }
    save_contacts(contacts)
    print("Contact added successfully.")

def edit_contact(contacts):
    unique_id = input("Enter the unique identifier of the contact to edit: ").strip()
    if unique_id not in contacts:
        print("Contact not found.")
        return

    name = input(f"Enter new name ({contacts[unique_id]['name']}): ").strip()
    phone = input(f"Enter new phone number ({contacts[unique_id]['phone']}): ").strip()
    email = input(f"Enter new email address ({contacts[unique_id]['email']}): ").strip()
    additional_info = input(f"Enter new additional information ({contacts[unique_id]['additional_info']}): ").strip()

    if email and not validate_email(email):
        print("Invalid email format.")
        return
    if phone and not validate_phone(phone):
        print("Invalid phone format. Use 10 digits.")
        return

    contacts[unique_id].update({
        "name": name if name else contacts[unique_id]['name'],
        "phone": phone if phone else contacts[unique_id]['phone'],
        "email": email if email else contacts[unique_id]['email'],
        "additional_info": additional_info if additional_info else contacts[unique_id]['additional_info']
    })
    save_contacts(contacts)
    print("Contact updated successfully.")

def delete_contact(contacts):
    unique_id = input("Enter the unique identifier of the contact to delete: ").strip()
    if unique_id in contacts:
        del contacts[unique_id]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    unique_id = input("Enter the unique identifier of the contact to search: ").strip()
    if unique_id in contacts:
        print("Contact details:", contacts[unique_id])
    else:
        print("Contact not found.")

def display_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    for unique_id, details in contacts.items():
        print(f"{unique_id}: {details}")

def export_contacts(contacts):
    with open("contacts_export.txt", "w") as file:
        for unique_id, details in contacts.items():
            file.write(f"{unique_id}: {details}\n")
    print("Contacts exported successfully.")

def import_contacts(contacts):
    try:
        with open("contacts_import.txt", "r") as file:
            for line in file:
                unique_id, details = line.strip().split(": ")
                contacts[unique_id] = eval(details)
        save_contacts(contacts)
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("Import file not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nWelcome to the Contact Management System!")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file *BONUS*")
        print("8. Quit")

        try:
            choice = int(input("Choose an option: ").strip())
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            edit_contact(contacts)
        elif choice == 3:
            delete_contact(contacts)
        elif choice == 4:
            search_contact(contacts)
        elif choice == 5:
            display_all_contacts(contacts)
        elif choice == 6:
            export_contacts(contacts)
        elif choice == 7:
            import_contacts(contacts)
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()