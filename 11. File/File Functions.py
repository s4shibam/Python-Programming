tf = input("Enter a file name along with its format type: ")

f = open(tf)
# We have no need to specify the "Mode" as a parameter as it takes "Read" mode by default.

print("Cursor position = ", f.tell())  # Tells present the Cursor position
print(f.readline())  # Prints line by line (This will print the very first line)

print("Cursor position = ", f.tell())  # Tells present the Cursor position
print(f.readline())  # Prints line by line (This will print the second line)

print("Cursor position = ", f.tell())  # Tells present the Cursor position
f.seek(0)  # Moves to Cursor position to the parameter value (here, 0)
print("New cursor position = ", f.tell())

# Will print the first line again as the cursor was pointed on 0
print(f.readline())
