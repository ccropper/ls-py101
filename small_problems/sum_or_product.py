# Write a program that asks the user to enter an integer greater than
# 0, then asks whether the user wants to determine the sum or the
# product of all numbers between 1 and the entered integer, inclusive.

integer = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum or "p" to compute the product: ')

if operation == "s":
    sum = 0
    for i in range(1, integer + 1):
        sum += i
    print(f"The sum of the integers between 1 and {integer} is {sum}.")
elif operation == "p":
    product = 1
    for i in range(1, integer + 1):
        product *= i
    print(f"The product of the integers between 1 and {integer} is {product}.")
else:
    print("You did not enter a valid choice.")
