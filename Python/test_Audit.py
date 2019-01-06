#!/usr/bin/env python3

# display a welcome message

product = 1
end_value = int(input("Enter a number: "))
for i in range(1, end_value):
    product = product * i
    i += 1
print("The product is ", product)
