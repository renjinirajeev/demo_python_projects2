# def matrixmultiply(matrix1,matrix2):
#     result=[[0,0,0],
#             [0,0,0],
#             [0,0,0]
#             ]
#     for i in range(len(matrix1)):
#         for j in range(len(matrix2[0])):
#             for k in range(len(matrix2)):          # for multiply and addition we use no of rows in 2nd matrix
#                result[i][j]+=matrix1[i][k]*matrix2[k][j]
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
# matrixmultiply(matrix1,matrix2)




# def matrixmultiply(matrix1,matrix2):
#     result=[
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     for i in range(len(matrix1)):
#         for j in range(len(matrix2[0])):
#             for k in range(len(matrix2)):
#                 result[i][j]+=matrix1[i][k]*matrix2[k][j]
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
# matrixmultiply(matrix1,matrix2)





# def matrixmultiply(matrix1,matrix2):
#     result=[
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     for i in range(len(matrix1)):
#         for j in range(len(matrix2[0])):
#             for k in range(len(matrix2)):
#                 result[i][j]=matrix1[i][k]*matrix2[k][j]
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
# matrixmultiply(matrix1,matrix2)


def matrix_mul(matrix1,matrix2):
    result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
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
matrix_mul(matrix1,matrix2)

