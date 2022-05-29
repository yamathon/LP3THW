def a(i, o):
    i = 0
    o = 6
    numbers = []
    for i in range(i, o):
        print(f"At the top i is {i}.")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}.")


    print("The numbers: ")
    for num in numbers:
        print(num)

a(0, 6)

# what happens if you remove the incrementor?
#
# absolutely nothing, script runs perfectly fine.
