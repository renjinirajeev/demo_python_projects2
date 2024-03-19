# def max_visited(matrix):
#     def dfs(matrix, i, j, visited):
#         if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0 or visited[i][j]:
#             return 0
#         visited[i][j] = True
#         count = 1
#         count += dfs(matrix, i + 1, j, visited)
#         count += dfs(matrix, i - 1, j, visited)
#         count += dfs(matrix, i, j + 1, visited)
#         count += dfs(matrix, i, j - 1, visited)
#         return count
#
#     max_count = 0
#     rows = len(matrix)
#     cols = len(matrix[0])
#     visited = [[False] * cols for _ in range(rows)]
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] != 0 and not visited[i][j]:
#                 max_count = max(max_count, dfs(matrix, i, j, visited))
#     return max_count
#
#
# # Example usage:
# matrix = [
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 0],
#     [1, 0, 0, 1]
# ]
#
# print(max_visited(matrix))  # Output: 6







def max_visit(matrix):
    def dfs(matrix,i,j,visited):
        if(i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]==0 or visited[i][j] ):
            return False
        visited[i][j]=True
        count=1
        count+=dfs(matrix,i+1,j,visited)
        count+=dfs(matrix,i-1,j,visited)
        count+=dfs(matrix,i,j+1,visited)
        count+=dfs(matrix,i,j-1,visited)
        return count
    max_count=0
    row=len(matrix)
    cols=len(matrix[0])
    visited=[[False]*cols for k in range(row)]
    for i in range(row):
        for j in range(cols):
            if (matrix[i][j]!=0 and not visited[i][j]):
                max_count=max(max_count,dfs(matrix,i,j,visited))
    return max_count
matrix=[
    [1,1,0,0],
    [1,0,0,1],
    [2,0,0,1],
    [1,0,1,2]
]


print(max_visit(matrix))

