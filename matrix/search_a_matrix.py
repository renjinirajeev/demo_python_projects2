# def search_element(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == target:
#                 return True
#     return False
#
# # Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# target_element = 5
#
# if search_element(matrix, target_element):
#     print(f"The element {target_element} is present in the matrix.")
# else:
#     print(f"The element {target_element} is not present in the matrix.")


# def searchMatrix(matrix,n):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if(matrix[i][j]==n):
#                 return i,j
#     return False
# matrix=[[1,2,3],[13,6,7],[9,0,1]]
# n=13
# result=searchMatrix(matrix,n)
# if result:
#     row,column=result
#     print(n,"found in",row,column)
# else:
#     print(n,'not found')
#
#
# def searchMatrix(matrix,n):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if(matrix[i][j]==n):
#                 return i,j
#     return False
# matrix=[[1,2,3,8],
#         [4,5,6,0],
#         [7,8,19,9]]
# n=9
# result=searchMatrix(matrix,n)
# if result:
#     row,column=result
#     print(n,'foun in the index',row,column)
# else:
#     print(n,'not found in index')


def search(matrix,n):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==n):
                return i,j
    return False
matrix=[
    [1,5,8,9],
    [3,4,66,87],
    [11,33,44,67]
]
n=66
result=search(matrix,n)
if result:
    row,column=result
    print(n,'found in the index',row,column)
else:
    print(n,"not found in the matrix")