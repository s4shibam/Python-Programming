# Faulty Calculator
"""
Design a calculator which will correctly solve all the problems except the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator and the two numbers as input from the user and then return the result
"""

n1 = int(input("Enter 1st no. = "))
n2 = int(input("Enter 2nd no. = "))

opt = input("Enter a operator (+ or - or * or /) = ")

if opt=="+":
    if (n1==56 and n2==9) or (n2==56 and n1==9):
        print("Addition Result = 77")
    else:
        print("Addition Result = ", n1+n2)

elif opt=="-":
    print("Subtraction Result = ", n1-n2)

elif opt=="*":
    if (n1==45 and n2==3) or (n2==45 and n1==3):
        print("Addition Result = 555")
    else:
        print("Addition Result = ", n1*n2)

elif opt=="/":
    if (n1==56 and n2==6) or (n2==56 and n1==6):
        print("Addition Result = 4")
    else:
        print("Addition Result = ", n1/n2)
