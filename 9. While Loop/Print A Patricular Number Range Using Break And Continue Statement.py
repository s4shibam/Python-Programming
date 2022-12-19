s = int(input("Enter the Starting no. = "))
e = int(input("Enter the Ending no. = "))
i = 0

if (e<s):
    print("Error Input")
else:
    while True:
        if (i<s):
            i+=1
            continue
        print(i, end=" ")
        if (i>=e):
            break

        i+=1