'''
Nested For Loop: Pattern 1: (Row Input = 5)
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

row = int(input("Enter no. of Row = "))

for i in range (row,0,-1):     # i=row, i>0, i++
    for j in range (1,i+1):    # j=1, j<i+1 [5+1], j++
        print(j, end=" ")
    print()