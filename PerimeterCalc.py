# Collect input on paper dimensions
# Validating input to ensure our input can be multiplied
# defining a generic function allows for consistent input of a given type
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid entry. Please enter an integer value.")
            continue
        else:
            return number


# Assign l and w by calling functions
l = get_number("Please enter the length of the paper in millimeters:")
w = get_number("Please enter the width of the paper in millimeters:")
# P = 2(l + w).
perimeter = 2 * (l + w)
# Concatenate the string with the output from our perimeter calculation
# convert int to str in order to join them in one line
print("The perimeter of the page is " + str(perimeter) + "mm")
