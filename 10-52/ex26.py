# needed to import modules for argv
from sys import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
# missing height input variable
height = input()
# missing right )
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

# misspelled variable 'filename'
txt = open(filename)

print("Here's your file {filename}:")
# mispelled variable 'txt'
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

# read is a function, not part of the variable name 'txt_again'
print(txt_again.read())


# single quote escape was needed here
print('Let\'s practice everything.')
# made this a one-line statement
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# missing right "
print("--------------")
print(poem)
# missing left "
print("--------------")


# missing 6 here
five = 10 - 2 + 3 - 6 
# missing right )
print(f"This should be five: {five}")

# missing colon
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    # missing division operator here
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# missing variable 'crates'
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# mispelled variable name 'start_point'
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
#mispelled cats as "cates"
cats = 30
dogs = 15


if people < cats:
    # missing ()
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# missing colon
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

# missing colon
if people <= dogs:
    # missing right "
    print("People are less than or equal to dogs.")


# == here instead of just one =. people is not being assigned a new value here.
if people == dogs:
    print("People are dogs.")


