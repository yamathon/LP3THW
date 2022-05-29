# create new variable with value of '30'
people = 30
# set new variable with value of '40'
cars = 40
# set new variable with value of '15'
trucks = 15


# sets conditions if fullfilled executes code beneath it
if cars > people:
    # this prints if there are more cars than people
    print("We could take the cars.")
# sets conditions if fullfilled executes code beneath it
elif cars < people:
    # this prints if there are less cars than people
    print("We should not take the cars.")
# sets conditions if fullfilled executes code beneath it
else:
    # this prints if there are the same cars as people
    print("We can't decide.")

# sets conditions if fullfilled executes code beneath it
if trucks > cars:
    # this prints if there are more cars than people
    print("That's too many trucks.")
# sets conditions if fullfilled executes code beneath it
elif trucks < cars:
    # this prints if there are more cars than trucks
    print("Maybe we could take the trucks.")
# sets conditions if fullfilled executes code beneath it
else:
    # this prints if there are the same trucks as cars
    print("We still can't decide.")

# sets conditions if fullfilled executes code beneath it
if people > trucks:
    # this prints if there are less trucks than people
    print("Alright, let's just take the trucks.")
# sets conditions if fullfilled executes code beneath it
else:
    # this prints if there are more trucks than people.
    print("Fine, let's stay home then.")
