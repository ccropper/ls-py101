import datetime

age = input("What is your age? ")
target = input("At what age would you like to retire? ")

years_left = int(target) - int(age)

current_year = datetime.datetime.now().year
retirement_year = current_year + years_left

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_left} years of work to go!")
