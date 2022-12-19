str = "Earth is round in shape"
print(str[::-1])  # ["string_name".[::-1]] --> Reverses a string.

strcpy = reversed(str)  # Reversing a string

print(strcpy)  # Prints address of the string.

for i in strcpy:  # Prints the string in reverse.
    print(i, end="")
