# given a number, sum multiples of 3 and 5 up to that number
def multisum(num):
    running_sum = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            running_sum += i
    return running_sum


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
