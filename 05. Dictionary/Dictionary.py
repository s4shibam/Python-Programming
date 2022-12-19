# Dictionary --> Key value pairs. Declared by {}

d1 = {}
print(type(d1))

name_title = {"Shibam": "Saha", "Sunabha": "Panda", "Pranab Saha": {
    "Office": "Employee", "Batch": "Sir", "Home": "Son"}}
print(name_title)

# Updating key pairs in selected array Type 1
name_title["Vicky"] = "Kaushal"
print(name_title)

name_title["Katrina"] = "Kaif"  # Updating key pairs in selected array Type 1
print(name_title)

# Updating key pairs in selected array Type 2
name_title.update({"Salman": "Khan"})
print(name_title)

del name_title["Katrina"]   # Deleting element from a dictionary
print(name_title)

t = input("Input name to get title = ")
print(name_title[t])

d = input("Input location for identity of Pranab Saha = ")
print(name_title["Pranab Saha"][d])  # Dictionary in Dictionary
