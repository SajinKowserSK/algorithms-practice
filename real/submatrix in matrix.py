def submatrix(matrix, k):
    master = []
    submatrix = []

    for x in range(0, len(matrix)-k+1):
        row = []
        for y in range(0, len(matrix[x])-k+1):
            row.append(matrix[x][y])

        submatrix.append(row)
        if (x + 1) % k == 0:
            master.append(submatrix)
            submatrix = []

    return master


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(submatrix(matrix, 2))


[[[1, 2],
  [4, 5]]]