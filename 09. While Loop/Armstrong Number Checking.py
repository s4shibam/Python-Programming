print("Armstrong Number Checking")
num = int(input("Enter a number to check = "))
dnum = num
sum = 0
while(num>0):
    n=num%10
    sum+=(n**3) # "**" is used to get power value ("**" = "^").
    num//=10 # "//" is used to get integer type return.

if (sum == dnum):
    print(dnum, "is an Armstrong number.")
else:
    print(dnum, "is Not an Armstrong number.")