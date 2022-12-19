import functools

numbs = [1, 2, 3, 4, 5]

cum_sum = functools.reduce(lambda x,y: x+y, numbs)
cum_mul = functools.reduce(lambda x,y: x*y, numbs)

print("1+2+3+4+5 = ", cum_sum)
print("1*2*3*4*5 = ", cum_mul)