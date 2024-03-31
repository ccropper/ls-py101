def crunch(string):
    result = ""
    last_letter = ""
    index = 0

    while index < len(string):
        if string[index] != last_letter:
            result += string[index]
            last_letter = string[index]
        index += 1

    return result

    pass


# These examples should all print True
print(crunch("ddaaiillyy ddoouubbllee") == "daily double")
print(crunch("4444abcabccba") == "4abcabcba")
print(crunch("ggggggggggggggg") == "g")
print(crunch("abc") == "abc")
print(crunch("a") == "a")
print(crunch("") == "")
