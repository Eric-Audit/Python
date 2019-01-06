#!/usr/bin/env python3
    
number = 0
count = 0

def get_number():
    global number
    number = int(input("Please enter an integer between 1 and 5,000: "))

def get_prime(number):
    global count
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is NOT a prime number.")
                print("It has " + str(count) + " factors.")
                break
        else:
            print(number,"is a prime number.")
def factors(number):
    global count
    count = 0
    print("The factors of your number are:")
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            print(i)
            
def main():
    print("Prime Number Checker\n")
    choice = "y"
    while choice.lower() == "y":
        get_number()
        factors(number)
        get_prime(number)
        print()
        choice = input("Try again? (y/n): ")
        print()

if __name__ == "__main__":
    main()
