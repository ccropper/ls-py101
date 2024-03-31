def print_in_box(text, max=None):
    text = text[:max] if max else text

    length = len(text) + 2
    horizontal_border = "+" + ("-" * (length)) + "+"
    vertical_border = "|"

    print(horizontal_border)
    print(vertical_border + (" " * length) + vertical_border)
    print(vertical_border + " " + text + " " + vertical_border)
    print(vertical_border + (" " * length) + vertical_border)
    print(horizontal_border)


print_in_box("To boldly go where no one has gone before again.")
print_in_box("")

### test case for using max

print_in_box("To boldly go where no one has gone before again.", 10)
