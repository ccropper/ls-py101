def century(year):
    pass


"""
### P

problem statement: given a year, return its century with the appropriate suffix



input: an integer representing year
    - positive integer; may be into the future
output: The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

explicit requirements:
    - New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.
    - requires appropriate suffix

implicit requirements:
    - last 2 digits need to be considered in the case of 11th vs 1st

### E


print(century(2000) == "20th")          # century ends at years that end in 00
print(century(2001) == "21st")          # century begins at years that end with 01
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # 11th is 11th, not 11st even though last digit is a 1
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

### D

doesn't seem relevant

### A

two steps to this: need the century number, and need the suffix

century number:

integer floor divide year by 100. (e.g. 500 / 100 = 5th century) plus 1
unless the year ends in 00, in which case do not need to add 1


suffix:

figure out last 2 digits
figure out last digit

if last 2 digits is 11, 12, 13 ==> th

if last digit is 1 ==> st
if last digit is 2 ==> nd
if last digit is 3 ==> rd

return century number with suffix


"""


def century(year):
    # integer floor divide year by 100. (e.g. 500 / 100 = 5th century) plus 1

    # unless the year ends in 00, in which case do not need to add 1

    if year % 100 == 0:
        century = year // 100
    else:
        century = year // 100 + 1

    # suffix:

    # figure out last 2 digits
    # figure out last digit

    last_two_digits = century % 100
    last_digit = century % 10

    suffix = "th"

    # if last digit is 1 ==> st
    # if last digit is 2 ==> nd
    # if last digit is 3 ==> rd

    match last_digit:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"

    # if last 2 digits is 11, 12, 13 ==> th

    match last_two_digits:
        case 11 | 12 | 13:
            suffix = "th"

    # return century number with suffix

    return str(century) + suffix


print(century(2000) == "20th")  # True
print(century(2001) == "21st")  # True
print(century(1965) == "20th")  # True
print(century(256) == "3rd")  # True
print(century(5) == "1st")  # True
print(century(10103) == "102nd")  # True
print(century(1052) == "11th")  # True
print(century(1127) == "12th")  # True
print(century(11201) == "113th")  # True
