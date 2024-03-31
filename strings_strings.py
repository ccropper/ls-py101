def stringy(num):
    result = ""
    for i in range(num):
        if i % 2 == 0:
            result += "1"
        else:
            result += "0"

    return result


print(stringy(6) == "101010")  # True
print(stringy(9) == "101010101")  # True
print(stringy(4) == "1010")  # True
print(stringy(7) == "1010101")  # True
