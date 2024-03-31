from random import randint

name = input("What is your name? ")

age = randint(20, 100)

if not name:
    name = "Teddy"

print(f"{name} is {age} years old.")
