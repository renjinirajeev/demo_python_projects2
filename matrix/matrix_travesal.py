def traverse_matrix(matrix):
    visited_elements = set()
    max_element = float('-inf')

    rows = len(matrix)
    cols = len(matrix[0])

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def visit(i, j):
        nonlocal max_element
        if is_valid(i, j) and matrix[i][j] != 0 and (i, j) not in visited_elements:
            visited_elements.add((i, j))
            max_element = max(max_element, matrix[i][j])
            return 1 + visit(i + 1, j) + visit(i - 1, j) + visit(i, j + 1) + visit(i, j - 1)
        return 0

    total_visited = 0
    for i in range(rows):
        for j in range(cols):
            total_visited += visit(i, j)

    return total_visited


# Example usage:
matrix = [
    [1, 2, 0, 0],
    [9 , 4, 5, 0],
    [9, 8, 9, 10]
]

result = traverse_matrix(matrix)
print("Number of elements visited:", result)
