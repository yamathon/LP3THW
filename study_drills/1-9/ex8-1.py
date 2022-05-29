# assigns string with four placeholders for embedding values inside
formatter = "{} {} {} {}"

# prints the following numbers, formatted in a string by the placeholders
print(formatter.format(1, 2, 3, 4))
# prints the following strings, formatted in a string by the placeholders
print(formatter.format("one", "two", "three", "four"))
# prints the following Booleans, formatted in a string by placeholders
print(formatter.format(True, False, False, True))
# prints the string value of variable, formatted in a string by placeholders
print(formatter.format(formatter, formatter, formatter, formatter))
# prints bits of string formatted in a single string by placeholders
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
