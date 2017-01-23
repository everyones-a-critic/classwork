# Printing 5 state tax rates
# Arbitrarily chosen by virtue of being states I've lived in
from sys import platform as _platform
# If running this in a Linux terminal,
# (or bash in Mac OSX)
# you get nicely colored output
if _platform.startswith("linux") or _platform.startswith("darwin"):
    class TextColor:
        green = '\033[1;32m'
        blue = '\033[38;5;39m'
        red = '\033[38;5;160m'
        none = '\033[0m'
    def printGreen(text):
        print(TextColor.green + text + TextColor.none)
    def printBlue(text):
        print(TextColor.blue + text + TextColor.none)
    def printRed(text):
        print(TextColor.red + text + TextColor.none)
    printBlue("Sales Tax Rates")
    printBlue("----------------")
    printRed("California = 7.5%")
    printRed("Florida = 6%")
    printGreen("Oregon = 0%")
    printRed("Virginia = 5.3%")
    printRed("Washington D.C. = 5.75%")
# I don't know enough about curses/ANSI for Windows
elif _platform.startswith("win"):
    print("Sales Tax Rates")
    print("----------------")
    print("California = 7.5%")
    print("Florida = 6%")
    print("Oregon = 0%")
    print("Virginia = 5.3%")
    print("Washington D.C. = 5.75%")
else:
    print("What are you running this on?")
