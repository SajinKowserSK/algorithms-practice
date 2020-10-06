def lilysHomework(arr):
    if arr is None or len(arr) == 0:
        return 0

    swaps = 0
    for x in range(0, len(arr)):
        lowest = arr[x]
        indice = x

        for y in range(x, len(arr)):

            if arr[y] < lowest:
                lowest = arr[y]
                indice = y

        if indice != x:
            swap(arr, x, indice)
            swaps += 1

    return swaps

def swap(arr, i_1, i_2):
    tmp = arr[i_1]
    arr[i_1] = arr[i_2]
    arr[i_2] = tmp

    return arr


print(lilysHomework([7,15,12,3]))