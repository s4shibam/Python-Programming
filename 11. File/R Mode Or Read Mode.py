tf = input("Enter a file name along with its format type: ")

f = open(tf, "r")
content = f.read()
print("\n", content)
f.close()
print("--------------------------------------------------")

f = open(tf, "r")
print("\nPrinting the file using \"f.readline\" function:\n")
print(f.readline())  # Prints line by line (This will print the very first line)
print(f.readline())  # Prints line by line (This will print the second line)

# If "f.readline()" is used again after the previous one, then the third line will be printed.

f.close()
print("--------------------------------------")

print("\nPrinting the .txt file in Text mode:\n")
# r mode is basically rt mode itself, means by default it prints in text (t) format
f = open(tf, "rt")
content = f.read()
print(content)

f.close()
print("----------------------------------------")

print("\nPrinting the .txt file in Binary mode:\n")
f = open(tf, "rb")
content = f.read()
print(content)

f.close()
print("-----------------------------------------")

print("\nPrint till certain character!!!!")
n = int(input("Read till the charcter no. = "))
f = open(tf, "r")
content = f.read(n)
print(content)

f.close()
print("----------------")

f = open(tf, "rt")
content = f.read()
print("Print by line:\n")

for line in content:
    print(line)

f.close()
