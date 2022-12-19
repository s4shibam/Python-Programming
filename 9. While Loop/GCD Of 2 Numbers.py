a = int(input("Enter 1st Number = "))
b = int(input("Enter 2nd Number = "))

if (a > b):
    dup_a = a
    while (a > 0):
        if (b % a == 0 and dup_a % a == 0):
            print("GCD = ", a)
            break
        a -= 1
elif (b > a):
    dup_b = b
    while (b > 0):
        if (a % b == 0 and dup_b % b == 0):
            print("GCD = ", b)
            break
        b -= 1
else:
    print("GCD = ", a)
