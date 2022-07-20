# import the sys module from the argv package
from sys import argv

# create two new variables as part of argv
script, filename = argv

# print string, with embedded value of argv
print(f"We're going to erase {filename}")
# print strings
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# prompt user for input, either CTRL-C or ENTER.
input("?")

# print string
print("Opening the file...")
# need to open file by creating new variable, in 'w' mode.
target = open(filename, 'w')

# print string
print("Truncating the file. Goodbye!")
# truncate the file associated withi target
target.truncate()

# print string
print("Now I'm going to ask you fo three lines.")

# prompt user for input for three lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# print string
print("I'm going to write these to the file.")

# write to target the user input for lines1-3
# write newline to target for each line so that they
#are not printed on the same line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# print string
print("And finally, we close it.")
# close the file associated with target.
target.close()