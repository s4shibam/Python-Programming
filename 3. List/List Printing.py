grocery = ["Gram Flour", "Top Biscuit", "Basmati Rice", "Cashewnuts", 75, 10, "Potato", "Cheese"]
print(type(grocery))
print(grocery)

print(grocery[0])  # Prints 0th index String

print(grocery[4])  # Prints 4th index String

print(grocery[1])  # Prints 1st index String

print(grocery[0:])  # Prints full list

print(grocery[:8])  # Prints full list

print(grocery[0:3])  # Prints 0 to 2 index string

print(grocery[4:7])  # Prints 4 to 6 index string

print(grocery[0:8:2])  # Prints 0 to 7 index string skipping 1 string

print(grocery[0:8:3])  # Prints 0 to 7 index string skipping 2 strings

print(grocery[::-1])  # Reverses the string

grocery.append(420)  # Adds string at the end of selected list
grocery.append("Garam Masala")

print(grocery)

grocery.insert(3, 50)  # Inserts given value at desired index
print(grocery)

grocery.pop()  # Deletes last index value
print(grocery)

grocery.remove("Gram Flour")  # deletes given value
print(grocery)
