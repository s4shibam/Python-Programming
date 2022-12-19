tf = input("Enter a file name to create, along with its type: ")

f = open(tf, "r+")
a = f.read()

print(a)  # This prints that how much character has been inputted through the write mode.

f.write(input("Enter a line to append in the file: "))
f.close()
