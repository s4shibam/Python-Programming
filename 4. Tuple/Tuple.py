# Tuple --> It is Immutable (cannot change) list. denoted by parentheses ().

tp1 = (1, 2, 3)
print(type(tp1))
print(tp1)

# tp1[1]= 12 --> Not possible because "tp1" is a Tuple.

tp2 = (1)  # Single value in a tuple, does not declare as a tuple (Limitation).
print(tp2)

tp3 = (1,)  # An extra Comma (",") makes single input list into a Tuple.
print(tp3)

tpl = list(tp1)
print((type(tpl)))
print(tpl)

tp4 = tp1 * 2
print(tp4)