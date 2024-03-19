def TransposeMatrix(matrix):
    # transpose=[]
    # for j in range(len(matrix[0])):
    #     for i in range(len(matrix)):
    #         transpose[i][j]=matrix[j][i]
    transpose=[[matrix[j][i] for j in range (len(matrix))] for i in range(len(matrix[0])) ]
    # print(transpose)
    for r in transpose:
        print(r)
matrix=[
    [1,2,3],
    [4,5,6],
    [3,6,5],
    [6,8,9]
]
TransposeMatrix(matrix)
