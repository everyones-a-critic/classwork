# Collect input on paper dimensions
# Validating input to ensure our input can be multiplied


def get_number(message):
    while True:
        try:
            n = int(input(message))
        except TypeError:
            print("Invalid entry. Please enter an integer value.")
            continue
        else:
            return n
            break


# Assign l and w by calling functions
l = get_number("Please enter the length of the paper in millimeters:")
w = get_number("Please enter the width of the paper in millimeters:")
# P = 2(l + w).
perimeter = 2 * ( l + w )
# Concatenate the string with the output from our perimeter calculation
# convert int to str in order to join them in one line
print("The perimeter of the page is " + str(perimeter) + "mm")
