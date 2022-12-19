tf = input("Enter a file name to create, along with its type: ")

f = open(tf, "r+")
a = f.read()

# This prints that how much character has been inputted through the write mode.
print(a)

f.write(input("Enter a line to append in the file: "))
f.close()
