def kxk_matrix(matrix, size):
    numbers = matrix
    submatrices = []

    side = 0
    down = 0

    divisons = int(len(numbers[0]) / size)

    while side < len(numbers[0]):
        sub_matrix = []

        for y in range(0, divisons):

            for x in range(0, len(numbers)):
                curr_arr = numbers[x]
                slice = curr_arr[side:side+size]
                for num in slice:
                    sub_matrix.append(num)


                if len(sub_matrix) == size * size:
                    submatrices.append(sub_matrix)
                    sub_matrix = []

            side = side + size

    return submatrices

print(kxk_matrix(
[[1,2,3,4,5,6],
 [10,11,12,13,14,15],
 [19,20,21,22,23,24]]
    , 2))


