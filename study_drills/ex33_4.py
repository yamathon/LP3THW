def a(i, o, k):
    numbers = []
    while i < o:
        print(f"At the top i is {i}.")
        numbers.append(i)
        i += k
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}.")

    print("The numbers: ")
    for num in numbers:
        print(num)

a(10, 50, 10)

print("Let's say you have a bunch of sizes of gold bars...")
print("RETURN to continue, CTRL-C to abort.")
input()
a(1, 7777, 77)
