def a(i, o):
    i = 0
    o = 6
    numbers = []
    while i < o:
        print(f"At the top i is {i}.")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}.")


    print("The numbers: ")
    for num in numbers:
        print(num)

a(0, 6)
