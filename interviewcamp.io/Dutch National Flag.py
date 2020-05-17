# Level: MediumYou are given an array of integers and a pivot. Rearrange the array in the following order:
# [all elements less than pivot, elements equal to pivot, elements greater than pivot]
# For example,a = [5,2,4,4,6,4,4,3] and pivot = 4 --> result = [3,2,4,4,4,4,5,6].

def arrange(arr, pivot):
    startBoundary = 0
    endBoundary = len(arr)-1

    x = 0
    while x <= endBoundary:
        curr = arr[x]
        if curr < pivot:
            swap(x, startBoundary, arr)
            startBoundary = startBoundary + 1
            x = x + 1

        # don't update counter here since you might swap into the before pivot position
        # an elem greater than pivot ie [5,4,6] -> [6,4,5] needs to be inspected again
        elif curr > pivot:
            swap(x, endBoundary, arr)
            endBoundary = endBoundary - 1


        else:
            x = x + 1

    return arr

def swap(pos1, pos2, arr):
    tmp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = tmp
    return arr


print(swap(1,0,[1,2]))
print(arrange([6,4,1], 4))
