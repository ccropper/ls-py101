def greetings(lst, dct):
    greeting = (
        "Hello, "
        + " ".join(lst)
        + "! Nice to have a "
        + dct["title"]
        + " "
        + dct["occupation"]
        + " around."
    )
    return greeting


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
