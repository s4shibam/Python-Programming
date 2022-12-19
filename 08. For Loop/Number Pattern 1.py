'''
Nested For Loop: Pattern 1: (Row Input = 5)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

row = int(input("Enter no. of Row = "))

for i in range(1, row+1):     # i=1, i<row+1 [5+1], i++
    for j in range(1, i+1):   # j=1, j<i+1, j++
        print(j, end=" ")
    print()
