shop = ["Sunsilk Shampoo", "Dove Body Wash",
        "Wildstone Soap", "Envy Perfume", "Nivea Face Cream"]

# Only Even positioned items are needed.
i = 0
for item in shop:
    if i % 2 == 0:
        print(f"Buy {item}")
    i += 1
print()

# Enumerate function help to shorten a code as it locates the indexes and items both in a list.
for index, item in enumerate(shop):
    if index % 2 == 0:
        print(f"Buy {item}")
