a = int(input("Enter a Number = "))
rev = 0

while (a > 0):
    rem = a % 10
    rev = (rev*10) + rem
    a //= 10

print("Reverse of that no. is = ", rev)
