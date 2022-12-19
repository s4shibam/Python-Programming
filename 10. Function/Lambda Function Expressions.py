"""
Python Lambda Functions are anonymous function means that the function is without a name.
As we already know that the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python.

Pros: To make one line function without using a function!!
"""

add = lambda x, y: x + y
minus = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

a, b = input("Enter two numbers = ").split()
a = int(a)
b = int(b)


print("Addition Result = ", add(a, b))
print("Subtraction Result = ", minus(a, b))
print("Multiplication Result = ", mul(a, b))
print("Division Result = ", div(a, b))
