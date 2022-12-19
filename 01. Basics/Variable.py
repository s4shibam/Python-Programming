var1 = "Hello! I am learning Python! "
var2 = 123
var3 = 12.34
var4 = "Python is used in Machine learning, AI etc."
var5 = "100 "
var6 = "105"

print(type(var1))  # (type(variable name)) --> Identifies Class Type
print(type(var2))
print(type(var3))

print(var2 + var3)  # Sum of integer and float
print(var1 + var4)  # Concatenate two strings

print(var5 + var6)  # Numbers considered as a string as they are under double quote.
print(int(var5) + int(var6))  # Explicit type casting. Forcefully converted into Integer type from String type.

print(10 * "Shibam Saha\n")  # Printing same word for 10 times (10 * "string" )

print(10 * str(int(var5) + int(var6)))
# Taking a number input as a string, then by explicit type casting, converting it into integer type,
# then after addition, again type casting done and result has been converted into string,
# then using a command (10 * "string")it has been printed for 10 times.
