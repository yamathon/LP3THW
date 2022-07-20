# create new function, two arguments to embed in a bunch of strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print string
print("We can just give the function numbers directly:")
# call function with integers as arguments
cheese_and_crackers(20, 30)

# print string
print("OR, we can use variables from our script:")
# create new variables with values of integers
amount_of_cheese = 10
amount_of_crackers = 50

# call function with variables whose values are integers as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print string
print("We can even do math inside too:")
# call function with math as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# print string
print("And we can combine the two, variables and math:")
# call function with math consisting of values of variables and integers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)