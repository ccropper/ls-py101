def oddities(lst):
    results = []
    for i, _ in enumerate(lst):
        if i % 2 == 0:
            results.append(lst[i])
    return results


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])  # True
print(oddities(["abc", "def"]) == ["abc"])  # True
print(oddities([123]) == [123])  # True
print(oddities([]) == [])  # True

"""
LS solution:

def oddities(lst):
    return lst[::2]
    
"""
