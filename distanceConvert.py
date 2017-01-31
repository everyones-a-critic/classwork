# Defining constants
# Maintaining same significant digits for each conversion
METER_TO_LEAGUE = 0.000179986
METER_TO_FOOT = 3.280839895
METER_TO_YARD = 1.093613298

# Defining generic input function
# This time validating that it's not a string
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Invalid entry. Please enter an integer or float value.")
            continue
        else:
            return number


# Defining a single function for conversion
# This way it can be expanded upon if further conversions are required
def convert_meters(ratio):
    convertedNumber = distanceInMeters * ratio
    return convertedNumber


distanceInMeters = get_number("Please enter a distance in meters:")
print("Distance in Feet:")
print(str(convert_meters(METER_TO_FOOT)) + " ft")
print("Distance in Yards:")
print(str(convert_meters(METER_TO_YARD)) + " yd")
print("Distance in Leagues:")
print(str(convert_meters(METER_TO_LEAGUE)) + " leag")



