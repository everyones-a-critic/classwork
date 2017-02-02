# Defining sentences
class sentence:
    MIN = "two years"
    LOW = "five years"
    HIGH = "ten years"
    MAX = "life"


# Take input and validate it
# ValueError is a python built in exception
# ValueError will return if input is wrong data type,
# in addition to user defined behavior.
def get_number(inputPrompt):
    while True:
        try:
            number = float(input(inputPrompt))
            if number < 0:
                #inputError = ValueError("The value should be positive")
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter a value in grams.")
            continue
        else:
            return number


# Calculate sentence based on grams
def calc_sentence():
    grams = get_number("How many grams of chocolate were in the offender's posession? ")
    if grams <= 28:
        return sentence.MIN
    elif grams < 60:
        return sentence.LOW
    elif 60 <= grams <= 100:
        return sentence.HIGH
    else:
        return sentence.MAX
# Outputting the Sentence
print("This offender shall be sentenced to " + calc_sentence() + " in prison.")