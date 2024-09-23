def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(5, 1, 18)
result2 = get_matrix(3, 8, 15)
result3 = get_matrix(4, 3, 21)
print(result1)
print(result2)
print(result3)

