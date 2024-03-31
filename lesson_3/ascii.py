# For this practice problem, write a program that outputs The
# Flintstones Rock! 10 times, with each line indented 1 space to the
# right of the line above it.

phrase = "The Flintstones Rock!"

for space in range(0, 10):
    print((" " * space) + phrase)
