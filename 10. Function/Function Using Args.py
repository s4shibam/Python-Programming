# *args --> The special syntax *args in function definitions in python is used to pass a variable number of
# arguments to a function. It is used to pass a non-key worded, variable-length argument list.

def topper_boys(heading, *args):
    print(heading)
    for items in args:
        print(items)


statement = "Students (Batch 2020-2024) placed in top MNC's in USA:"
name = ["Abhirup", "Avilash", "Parthib", "Jyotipriya", "Soumyadeep", "Soumesh"]

topper_boys(statement, *name)
