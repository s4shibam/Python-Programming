# Write a program that asks the user for a number and prints a countdown from
# that number to zero using while loop.

num = int(input("Enter a number to start countdown = "))

print("\nCoundown upto Zero = ")

while(num>=0):
    print(num)
    num-=1