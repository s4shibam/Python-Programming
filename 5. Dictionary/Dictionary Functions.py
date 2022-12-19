d1 = {"Shibam": "Saha", "Sunabha": "Panda", "Pranab": "Saha", "Kaushik": "Paul"}
print("d1 = ", d1)

d2 = d1.copy()  # Shallow copy --> d1 copied to d2 (Now d1 and d2 are individual).

print("Printing Keys = ", d1.keys())    # Prints Keys
print("Printing Items = ", d1.items())  # Prints Key pairs

del d2["Pranab"]
print("d2 = ", d2)

print("d1 = ", d1)



d4 = d1     # This means d4 is as same as d1, whatever action is taken with d1, it will be reflected in d4 vice versa.
del d4["Sunabha"]   # Deleting "Sunabha" from d4 will alse delete it from d1.
print("d4 = ", d4)
print("d1 = ", d1)

del d1["Kaushik"]   # Deleting "Kaushik" from d1 will alse delete it from d4.
print("d1 = ", d1)
print("d4 = ", d4)

print(d1.get("Shibam")) # This prints the value



