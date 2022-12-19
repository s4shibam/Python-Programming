dec_num = int(input("Enter a Decimal no. = "))
dnum = dec_num
a = []
i = 0
while (dec_num > 0):
    rem = dec_num % 2
    a.append(rem)
    i += 1
    dec_num = dec_num // 2

if (dnum == 0):
    print("Binary = 0")
else:
    print("Binary = ", *a[::-1], sep='')  # Prints a list without brackets and commas
