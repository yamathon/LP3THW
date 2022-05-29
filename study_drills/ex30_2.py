# changed from 30 to 100000
people = 100000
# changed from 40 to 100
cars = 100
# changed from 15 to 20000
trucks = 20000


if cars > people:
    print("We could take the cars.")
elif cars < people:
    # this will be printed
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    # this will be printed
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    # this will be printed
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# predicted output:
# We should not take the cars.
# That's too many trucks.
# Alright, let's just take the trucks.
