bin_num = (input("Enter a Binary Number = "))
bin_len = len(bin_num)
bin_num = int(bin_num)
dec_num = 0
i=0
while(bin_num > 0):
    if (i != bin_len):
        rem = bin_num%10
        dec_num = dec_num + (rem * (2**i))
        bin_num//=10
        i+=1

print("Decimal = ", dec_num)
