# define new variable with value of 10
types_of_people = 10
# define new variable as string with formatted variable of 10
x = f"There are {types_of_people} types of people."

# define new variable with string
binary = "binary"
# define new variable with string
do_not = "don't"
# define new variable as string with formatted strings "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."

# prints x's string
print(x)
# prints y's string
print(y)

# informative statement to the user with formatted string from {x}
print(f"I said: {x}")
# informative statement to the user with formatted string from {y}
print(f"I also said: '{y}'")

# define new variable with boolean value of False
hilarious = False
# define new variable as string with a placeholder to format a variable in
joke_evaluation = "Isn't that joke so funny?! {}"

# prints joke_evaluation's string formatted with "hilarious" in the {} placeholder
print(joke_evaluation.format(hilarious))

# define new variable as string
w = "This is the left side of..."
# define new variable as string
e = "a string with a right side."

# prints strings from w and e with NO newline
print(w + e)
