v = 100
v3 = 200
v4 = 300
# This is a Global variable. It can be used in a user defined Function also if in case
# there, this variable is not pre-defined.

print("Global Value, v =", v)
print("Global Value, v3 =", v3)
print("Global Value, v4 =", v4)


def fun1():
    v = 50  # Local variable
    v2 = 10  # Local variable ......(1)
    # v3 = v3 + v3
    # As v3 is declared globally, so it is not possible to change its value without defining it in the function.
    global v4
    # Permission given to change the value of that global variable, v4
    v4 = v4 + v4  # ......(2)
    print("This statement is under function.")
    print("Value in Function fun1():")
    print("  Local Value, v =", v)
    print("  local Value, v2 =", v2)  # ......(1)
    print("  Local Value, v3 =", v3)
    print("  Local Value, v4 =", v4)  # ......(2)


print(fun1())
# print("v2 = ", v2) # v2 can't be printed as it is not declared globally!!! ......(1)

print("Global Value after function call, v4 =", v4)  # ......(2)
# v4 value will be changed as it was changed in function and this statement is stated after calling the function.
# print("v2 = ", v2) # v2 can't be printed as it is not declared globally!!!
