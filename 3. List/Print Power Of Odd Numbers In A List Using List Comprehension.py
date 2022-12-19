"""
List comprehension is an elegant way to define and create a list in python. We can create lists just like
mathematical statements and in one line only. The syntax of list comprehension is easier to grasp.

A list comprehension generally consists of these parts :

1. Output expression,
2. Input sequence,
3. A variable representing a member of the input sequence and
4. An optional predicate part.
"""

lst = [x ** 2 for x in range(1, 21) if x % 2 == 1]

"""
here, x ** 2 is output expression, (Same as x^2)
      range (1, 11)  is input sequence,
      x is variable and
      if x % 2 == 1 is predicate part.
"""

print(lst)
