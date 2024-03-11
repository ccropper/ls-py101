# Build a program that asks the user to enter the length and width
#  of a room, in meters, then prints the room's area in both square
# meters and square feet.
# Note: 1 square meter == 10.7639 square feet


def calculate_area(length, width):
    area_in_meters = length * width
    area_in_feet = area_in_meters * 10.7639
    print(
        f"The area of the room is {area_in_meters} square meters ({area_in_feet} square feet)."
    )


length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

calculate_area(length, width)
