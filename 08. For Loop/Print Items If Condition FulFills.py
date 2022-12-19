bag = ["Potato", "Tomato", 5, 23, 30, 45, 57, "Cabbage", 65, 76, 82, 91, 97, "Carrot"]

print("Greater than 50, numbers are = ")
for item in bag:
    if str(item).isnumeric() and item > 50:     # If items are number type and more than 50, then print it.
        print(item)
