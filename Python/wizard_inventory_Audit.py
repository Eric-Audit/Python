#!/usr/bin/env python3

def display_menu():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(wizard_inventory):
    i = 1
    for item in wizard_inventory:
        print(str(i) + ". " + item)
        i += 1
    print()

def grab(wizard_inventory):
    if len(wizard_inventory) == 0:
        item = input("Name: ")
        wizard_inventory.append(item)
        print(item + " was added.\n")
    elif len(wizard_inventory) < 4 and len(wizard_inventory) > 0:
        item = input("Name: ")
        wizard_inventory.append(item)
        print(item + " was added.\n")
    else:
        print("The wizard can only carry so much, drop something first.")
        print()
        
def edit(wizard_inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(wizard_inventory):
        print("invalid item number.\n")
    else:
        item = input("Updated Name: ")
        wizard_inventory.insert(number, item)
        item = wizard_inventory.pop(number-1)
        print("Item number " + str(number) + " was updated.\n")

def drop(wizard_inventory):
    number = int(input("Number: "))
    if len(wizard_inventory) < 1:
        print("The wizard has no more items! Go get something!")
        print()
    elif number < 1 or number > len(wizard_inventory):
        print("invalid item number, please pick 1-4.\n")
    else:
        item = wizard_inventory.pop(number-1)
        print(item + " was dropped.\n")
            
def main():
    wizard_inventory = ["staff", "hat", "scroll"]
              
    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show(wizard_inventory)
        elif command.lower() == "grab":
            grab(wizard_inventory)
        elif command.lower() == "edit":
            edit(wizard_inventory)
        elif command.lower() == "drop":
            drop(wizard_inventory)
        elif command.lower() == "exit":
            break
        else:
            print("This is unknown knowledge to even a wizard. please try again.\n")

    print("Your journey is over!")
            
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

