# Print all odd numbers from 1 to 99, inclusive, with each number on
# a separate line.

# Bonus Question: Can you solve the problem by iterating over just
# the odd numbers?

# for n in range(1,101,2):
#     print(n)

# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

start = int(input("What number should we start at? "))
end = int(input("What number should we start at? "))

for n in range(start, end + 1, 2):
    print(n)
