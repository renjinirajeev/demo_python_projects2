
r=int(int(input('rows:')))
c=int(int(input('cols:')))
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        k=int(input())
        a.append(k)
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end='')
    print()
