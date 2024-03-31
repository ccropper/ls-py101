def clean_up(words):
    cleaned_up_words = ""
    for i, char in enumerate(words):
        if char.isalpha():
            cleaned_up_words += char
        elif i == 0 or cleaned_up_words[-1] != " ":
            cleaned_up_words += " "
    return cleaned_up_words


print(clean_up("---what's my +*& line?") == " what s my line ")
# True
print(clean_up(""))
