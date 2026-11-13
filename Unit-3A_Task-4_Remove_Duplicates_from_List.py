"""list_data = [1, 2, 2, 3, 1, 4, 3]
unique = []

for item in list_data:
    if item not in unique:
        unique.append(item)

print("Original:", list_data)
print("Without duplicates:", unique)"""


matrix_a = [1, 2], [3, 4] # e.g. [[1, 2], [3, 4]]
matrix_b = [5, 6], [7, 8] # e.g. [[5, 6], [7, 8]]

rows = len(matrix_a)  # len(matrix_a)
cols =  len(matrix_a[0])  # len(matrix_a[0])

result = []
for i in range(rows):  # i in range(rows)
    row = []
    for j in range(cols):  # j in range(cols)
        row.append(____)  # matrix_a[i][j] + matrix_b[i][j]
    result.append(____)

print("Matrix A:", ____)
print("Matrix B:", ____)
print("Sum:", ____)