def max_sub_matrix_sum(matrix, size):

    submatrices = []
    side = len(matrix[0])

    for x in range(0, side):
        sub_matrix = []

        for y in range(0, len(matrix)):
            curr_arr = matrix[y]

            if x + size-1 < side:

                curr_slice_size = x + size
                curr_slice = curr_arr[x:curr_slice_size]

                for num in curr_slice:
                    sub_matrix.append(num)

                if len(sub_matrix) == size * size:

                    submatrices.append(sub_matrix)
                    sub_matrix.pop(0)
                    sub_matrix.pop(0)

        side = side + 1


    return submatrices

def max_submatrices(matrix, size):
    num_cols = len(matrix[0])
    num_rows = len(matrix)

    max_k = min(num_cols, num_rows)

    total_cases = 0
    for x in range(2, max_k):
        total_cases += (num_cols - size+1) * (num_rows - size+1)

    return total_cases


matrix = [[1,2,3,4,5,6],
 [10,11,12,13,14,15],
 [19,20,21,22,23,24]]

matrix2 = [[10,20,30,40,50,60,70,80,90],
           [11,22,33,44,55,66,77,88,99],
           [12,23,34,45,56,67,78,89,98]]


print(max_sub_matrix_sum(matrix2, 3))
print(len(max_sub_matrix_sum(matrix2, 3)))
print(max_submatrices(matrix2, 3))




