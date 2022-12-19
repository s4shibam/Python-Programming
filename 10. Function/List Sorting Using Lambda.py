l1 = [[32, 17], [21, 19], [9, 10], [43, 8], [90, 0]]

print(l1[1])

l1.sort(key=lambda x: x[1])  # This lambda function takes a sorted list input as "x", then returns "x[1]".
print("Sorted List = ", l1)
