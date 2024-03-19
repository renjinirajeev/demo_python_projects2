# r=int(input('enter no of rows:'))
# c=int(input('enter no of columns:'))
# matrix=[]
# for i in range(r):
#     a=[]
#     for j in range(c):
#         k=int(input())
#         a.append(k)
#     matrix.append(a)
# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j],end="")
#     print()


r=int(input("row:"))
c=int(input('col:'))
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