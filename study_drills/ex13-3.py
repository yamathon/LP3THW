from sys import argv

script, networth = argv

print("Supposedly you had:", networth, "networth.")
increase = int(input("By how much do you want to multiply it?  "))

new_networth = increase * int(networth)
print("Your new networth is now: ", new_networth)