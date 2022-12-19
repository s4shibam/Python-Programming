with open("Shibam 1.txt") as f:
    # With Open --> As same as the second function which is written below.
    a = f.readlines()
    print(a)

x = open("Shibam 1.txt")
z = x.readlines()
print(z)
x.close()
