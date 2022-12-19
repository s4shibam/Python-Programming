age_list = [["Salman Khan", 55], ["Vicky Kaushal", 33],
            ["Katrina Kaif", 38], ["Ranbir Kapoor", 39]]

age_dict = dict(age_list)
print(type(age_dict))
print(age_dict, "\n")

for name, age in age_dict.items():
    print("Age of", name, "is", age, "Years.")

print("\n")

print("Name: ")
for name in age_dict:
    print(name)

print("\n")

print("Age: ")
for name, age in age_dict.items():
    print(age)
