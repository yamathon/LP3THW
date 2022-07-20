# this script uses .read() and argv to read
#the file.

from sys import argv

script, targetfile = argv

print(f"Reading the file '{targetfile}'")

opentarget = open(targetfile)
print(opentarget.read())