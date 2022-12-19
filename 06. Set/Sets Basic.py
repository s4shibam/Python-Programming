s = set()  # Set --> A set is a collection of elements
print("'s' variable type = ", type(s))

set_using_list = set([1, 2, 3, 4, 5, 6, 7, 8, 9])  # defining Set using list
print("\n'set_using_list' variable type = ", type(set_using_list))
print(set_using_list)

print("\nSet s = ")
s.add(10)  # Adding values.
# This value will not be added as Set function only accepts unique values.
s.add(10)
print(s)
s.add(20)
print(s)
s.add(30)
print(s)
