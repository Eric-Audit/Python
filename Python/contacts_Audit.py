#!/usr/bin/env python3

import csv

FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
            
def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
        return contacts
    
def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])
    print()
    
def view_contact(contacts):
    try:
        number = int(input("Number: "))
    except ValueError:
        print ("You need to enter a number")
    else:
        if number < 1 or number > len(contacts):
            print("invalid contact number.\n")
        else:
            contact = contacts[number-1]
            print(contact)
        
    print()

def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

def delete_contact(contacts):
    try:
        number = int(input("Number: "))
    except ValueError:
        print ("You need to enter a number")
    else:
        if number < 1 or number > len(contacts):
            print("invalid contact number.\n")
        else:
            contact = contacts.pop(number - 1)
            write_contacts(contacts)
            print(contact[0] + " was deleted. \n")
    
                                
def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()


            
def main():          
    display_menu()
    contacts = read_contacts()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "view":
            view_contact(contacts)
        elif command.lower() == "add":
            add_contact(contacts)
        elif command.lower() == "del":
            delete_contact(contacts)
        elif command.lower() == "exit":
            break
        else:
            print("This is not a valid command. please try again.\n")

    print("Bye!")
            
# if started as the main module, call the main function
if __name__ == "__main__":
    main()
