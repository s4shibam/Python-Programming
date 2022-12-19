tf = input("Enter a file name to create, along with its type: ")

f = open(tf, "a")
a = f.write("Shibam is one of the best programmer.\n")

# This prints that how much character has been inputted by the write mode.
print(a)
f.close()
