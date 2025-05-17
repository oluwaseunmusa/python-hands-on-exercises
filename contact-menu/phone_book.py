#!/usr/bin/python3

import os
import getpass

# ------------------------- App Info -------------------------
app_requirements = """
--------------------------------------------------------------------
This is a Contact Book Application that lets users do the following:
--------------------------------------------------------------------
- Add Contacts
- View Contacts
- Search for Saved Contacts
- Delete Contacts 

-------------------------------------------------------
The code logic, requirements, and acceptance criteria:
-------------------------------------------------------
* Add, View, Search, and Delete contacts using input, lists, conditional statements, loops, and functions.
* Store all contacts in a list of dictionaries.
* Each contact must have name, phone number, and email.
* Use functions for each operation (add, view, search, delete).
* Use input() to interact with the user.
* Use loops to keep the program running until the user chooses to exit.
* Use if/else statements to handle choices and errors.

----------------------------------
Functionalities You Must Implement
----------------------------------
    - add_contact() — Add a new contact.
    - view_contacts() — Display all saved contacts.
    - search_contact() — Search for a contact by name.
    - delete_contact() — Delete a contact by name.
    - main_menu() — Show options and handle user choices in a loop.
"""

# ----------------------Application  Setup ----------------------
def sys_user():
    """ Function to get system username """
    return getpass.getuser()



def cls():
    """ Function to Clear screen """
    os.system('cls' if os.name == 'nt' else 'clear')

def message_header():
    """ Function to display welcome message """
    owner_contact = sys_user().capitalize()
    print('-' * 40)
    print(f"{owner_contact}, Welcome to the Contacts Book")
    print('-' * 40)
    print()


def contact_book__menu():
    """ Function to display contact book menu """
    cls()
    contact_menu = {
        1: 'Add Contact', 
        2: 'View Contacts', 
        3: 'Search Contact',
        4: 'Delete Contact',
        5: 'Exit'
    }
    for key, value in contact_menu.items():
        print(f"{key} : {value}")
    return contact_menu

# -------------------- Contact Functions --------------------
contact_dictionary = {}

# Add Contact Logic
def add_contact():
    """ This function allows user to save contact to the phone book """
    cls()
    print("+ Add New Contact")
    print("-" * 30)
    name = input("Enter name : ").strip()
    phone_number = input("Enter phone number : ").strip()

    if not name or not phone_number:
        print("Name and phone number cannot be empty.")
        return

    # Add the contact to the dictionary
    contact_dictionary[name] = phone_number
    cls()
    print(" Contact added successfully!\n")
    print("Current Contacts")
    print("-" * 30)
    for name, phone in contact_dictionary.items():
        print(f" {name} :  {phone}")
    print()


def view_contacts_book():
    """ Function to view contact """
    cls()
    if not contact_dictionary:
        print(" X No contacts found.")
        return

    print("Saved Contacts")
    print("-" * 30)
    # This enumerate the values in index form  and starts from 1
    for index, (key, value) in enumerate(contact_dictionary.items(), start=1):
        print(f"{index}: {key} :  {value}")
    print()

def search_contact_book():
    """ Function to search contact """
    cls()
    found = False
    search_contact = input("Enter name  or number to search: ").lower()
    for name , number in contact_dictionary.items():
        if search_contact in name.lower() or search_contact in number:
            print()
            print(f"Contact found!: {name} - {number}")
            found = True
            print("-" * 30)
    if not found:
        print("No matching contacts found.")
        return


def delete_contact_book():
    cls()
    for index, (key, value) in enumerate(contact_dictionary.items(), start=1):
        print(f"{index}: {key} :  {value}")
    print()

    found = False
    delete_contact = input("Enter contact name to delete: ").lower()
    for name , number in contact_dictionary.items():
        if delete_contact in name.lower() or delete_contact in number:
            print()
            del contact_dictionary[name]
            print(f"Contact deleted!: {name} - {number}")
            found = True
            print("-" * 30)
    if not found:
        print()
        print(f"{delete_contact} is not available for deletion.")
        return
    
    

# -------------------- Main Menu & Application Start --------------------

owner_contact = sys_user().upper()
print(app_requirements)

def main_menu():
    """ Main Menu Function """
    while True:
        message_header()
        contact_book__menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts_book()
            elif choice == 3:
                search_contact_book()
            elif choice == 4:
                delete_contact_book()
            elif choice == 5:
                print(f"Exiting... Goodbye {owner_contact}!")
                break
            else:
                print(f" Invalid choice {owner_contact}. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

        input(f"\n{owner_contact} Press Enter to return to the menu...")
        cls()

""" Logic to keep Main Menu Running """
while True:
    proceed = input("Press 1 to continue: ")
    if proceed == '1':
        cls()
        main_menu()
        break
    else:
        cls()
        print(f" You pressed {proceed}. Invalid choice. Try again.\n")