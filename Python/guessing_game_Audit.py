#!/usr/bin/env python3

def display_menu():
    print("The Wizard Inventory Program")
    print("show - Show all items")
    print("grab - Grab all items")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

def show(wizard_inventory):
    i = 1
    for item in show_items:
        print(str(i) + ". " + item
        i += 1
    print()

def grab(wizard_inventory):
    item = input("Name: ")
    wizard_inventory.append(item)
    print(item + " was added.\n")

def edit(wizard_inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(wizard_inventory):
        print("invalid item number.\n")
    else:
        item = input("Updated Name: ")
        wizard_inventory.append(item)
        item = wizard_inventory.pop(number-1)
        print("Item number" + number-1 " was updated\n")
        


def drop(wizard_inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(wizard_inventory):
        print("invalid item number.\n")
    else:
        item = wizard_inventory.pop(number-1)
        print(item + " was dropped.\n")
            
            

def main():
    inventory = ["staff", "hat", "scroll"]
              
    display_menu()

    while true:
        command = input(Command: ")
        if command.lower() == "show":
            show(wizard_inventory):
        else if command.lower() == "grab":
            grab(wizard_inventory):
        else if command.lower() == "edit":
            edit(wizard_inventory):
        else if command.lower() == "drop":
            drop(wizard_inventory):
        else if command.lower() == "exit":
            break
        else:
            print("This is unknown knowledge to even a wizard. please try again.\n")

    print("Your journey is over!")
            
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

