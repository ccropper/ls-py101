def xor(a, b):
    if a and b:
        return False
    if a and not b:
        return True
    if b and not a:
        return True
    if not a and not b:
        return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

"""
LS solution:

def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))

"""
