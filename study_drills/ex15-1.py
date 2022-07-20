# imports the sys package from the argv module
from sys import argv

# breaks argv into two variables for two parameters
script, filename = argv

# the file has to be opened first, so create new variable
txt = open(filename)

# print string, embedded variable
print(f"Here's your file {filename}:")
# print out value of 'txt' with the .read() function
print(txt.read())

# print out string
print("Type the filename again:")
# create new variable that will be assigned to the input
file_again = input("> ")

# the file has to be opened first, so create new variable
txt_again = open(file_again)

# print value of 'txt_again' with the .read() function
print(txt_again.read())