def average(a, b):
    """This function will calculate the Average of two numbers."""
    # Above line is called as Docstring, which defines the use of the function.
    avrg = (a + b) / 2
    print("Sum = ", a + b)
    return avrg


a = int(input("Enter 1st no. = "))
b = int(input("Enter 2nd no. = "))

print("Docstring: ", average.__doc__) # Prints Docstring.
print("Average = ", average(a, b))
