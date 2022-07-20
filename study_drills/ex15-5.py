filename = input("Enter filename: ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# There are these different scenarios in which
#input() is better than argv.  For argv, you
#can only call it once. As for input, you
#can call it as many times as you want in the
#program. Input may be better for most of the 
#time but argv is useful in the sense of 
#running python programs with arguments
#on the command line for faster execution times
#rather than typing in your arguments one by one
#or piece by piece.