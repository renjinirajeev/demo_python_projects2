def search(matrix, n):
    if not  matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while(left <= right):
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if (mid_value == n):
            return (mid // cols, mid % cols)  # Return row and column indices
        elif(mid_value < n):
            left = mid + 1
        else:
            right = mid - 1

    return False  # Element not found

# Example usage:
matrix = [
    [2, 4, 6, 8],
    [3, 6, 88, 0],
    [11, 43, 5, 7]
]

n= 43
result = search(matrix, n)

if result:
    print(n,'found in index',result)
else:
    print(n,"not found in matrix")


def search(matrix,n):
    row,cols=len(matrix),len(matrix[0])
    left,right=0,row*cols-1
    while(left<=right):
        mid=(left+right)//2
        mid_value=matrix[mid//cols][mid%cols]
        if(mid_value==n):
            return (mid//cols,mid%cols)
        elif(mid_value<n):
            left=mid+1
        else:
            right=mid-1
    return False
matrix=[
    [0,1,2,5],
    [6,8,9,10],
    [12,25,57,90]
]

n=25
result=search(matrix,n)
if result:
    print(n,'element found in the index',result)
else:
    print(n,'not found in the matrix')







































#
# def search(matrix, n):
#     if not  matrix or not matrix[0]:
#         return False
#
#     rows, cols = len(matrix), len(matrix[0])
#     left, right = 0, rows * cols - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         mid_value = matrix[mid // cols][mid % cols]
#
#         if mid_value == n:
#             return (mid // cols, mid % cols)  # Return row and column indices
#         elif mid_value < n:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return False  # Element not found
#
# # Example usage:
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
#
# n= 11
# result = search(matrix, n)

# if result:
#     print(n,'found in index',result)
# else:
#     print(n,"not found in matrix")
