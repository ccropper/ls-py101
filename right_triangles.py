def triangle(height):
    for row in range(1, height + 1):
        spaces = (height) - row
        stars = row
        print(" " * spaces + "*" * stars)


triangle(5)
