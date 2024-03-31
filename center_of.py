def center_of(string):
    length = len(string)
    if length % 2 == 1:
        start = int(length / 2)
        stop = int(length / 2) + 1
        return string[start:stop]
    else:
        start = int(length / 2) - 1
        stop = int(length / 2) + 1
        return string[start:stop]


print(center_of("I Love Python!!!") == "Py")  # True
print(center_of("Launch School") == " ")  # True
print(center_of("Launchschool") == "hs")  # True
print(center_of("Launch") == "un")  # True
print(center_of("Launch School is #1") == "h")  # True
print(center_of("x") == "x")  # True
