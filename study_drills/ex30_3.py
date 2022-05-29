people = 30
cars = 40
trucks = 15


if cars > people or trucks < cars:
    print("We could take the cars.")
elif cars < people or trucks > cars:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars or cars > trucks:
    print("That's too many trucks.")
elif trucks < cars or cars < trucks:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks and people > cars:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
