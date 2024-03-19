# def matrix_add(matrix1,matrix2):
#     result=[[0,0,0],
#             [0,0,0],
#             [0,0,0]]
#     if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
#         print("matrix cannot be added")
#     else:
#         for i in range(len(matrix1)):
#             for j in range(len(matrix1[0])):
#                 result[i][j]=matrix1[i][j]+matrix2[i][j]
#     for r in result:
#         print(r)
# matrix1=[
#     [1,2,3],
#     [4,6,7],
#     [8,3,6]
# ]
# matrix2=[
#     [5,8,2],
#     [5,7,3],
#     [8,9,3]
# ]
# matrix_add(matrix1,matrix2)
#



# def matrixadd(matrix1,matrix2):
#     result=[
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
#         print('matrix cannot add')
#     else:
#         for i in range(len(matrix1)):
#             for j in range(len(matrix1[0])):
#                 result[i][j]=matrix1[i][j]+matrix2[i][j]
#     for r in result:
#         print(r)
# matrix1 = [
#         [1, 2, 3],
#         [4, 6, 7],
#         [8, 3, 6]
#     ]
# matrix2 = [
#         [5, 8, 2],
#         [5, 7, 3],
#         [8, 9, 3]
#     ]
# matrixadd(matrix1,matrix2)


def matrixadd(matrix1,matrix2):
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
        print("cannot add the matrix")
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result[i][j]=matrix1[i][j]+matrix2[i][j]
        for r in result:
            print(r)
matrix1 = [
        [1, 2, 3],
        [4, 6, 7],
        [8, 3, 6]
    ]
matrix2 = [
        [5, 8, 2],
        [5, 7, 3],
        [8, 9, 3]
    ]
matrixadd(matrix1,matrix2)

