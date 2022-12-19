# Write A Program To Read The Numbers Until -1 Is Encountered.
# Find The Average Of Positive And Negative Numbers Entered By The User Using While Loop.

i = 0
sum = 0
while (1):
    num = int(input("Enter a no. = "))
    if (num != -1):
        i = i+1
        sum = sum + num
    else:
        break

print("\nSum of the entered numbers is = ", sum)
print("Average of the entered", i, "numbers is = ", sum/i)
