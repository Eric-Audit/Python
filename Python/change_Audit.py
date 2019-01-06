#!/usr/bin/env python3
print("Change Calculator")
print()

#While loop to allow user to test multiple amounts
choice = "y"
while choice.lower() == "y":

    #get a dollars variable from the user
    dollars = float(input("Enter dollar amount (for example, .17, 7.17): "))
    print()
    
    #convert dollars variable into cents
    dollars = dollars * 100
    
    #rename the variable so it is easier to understand
    coins = dollars
    
    #use interger divison to get a remainder that will == quarters amount
    quarters = coins // 25

    #use a chain function to force quarters to display as an int
    print ("Quarters: " + str(int(quarters)))

    #set cents to the remainder of quarters
    coins = coins % 25
    
    #use interger divison to get a remainder that will == dimes amount
    dimes = coins // 10

    #use a chain function to force dimes to display as an int
    print ("Dimes: " + str(int(dimes)))
    
    #set cents to the remainder of dimes
    coins = coins % 10

    #use interger divison to get a remainder that will == nickels amount
    nickels = coins // 5

    #use a chain function to force nickels to display as an int
    print ("Nickels: " + str(int(nickels)))

    #set cents to the remainder of nickels
    coins = coins % 5

    #use round and division to increase python accuracy 
    pennies = round (coins / 1)
    
    print ("Pennies: " + str(pennies))
    print()    

    choice = input("Continue? (y/n): ")
    print()

print("Bye!")

