# shortest unsorted
# identify dip
# identify bump
# identify minimum in that subarray arr[dip:bump]
# go left from the minimum
# return minimum:bump+1
def find(arr):
    if arr is None or len(arr) == 0:
        return None

    dip = None
    for x in range (1, len(arr)):
        if arr[x] < arr[x-1]:
            dip = x
            break

    if dip is None:
        return None

    for x in range(len(arr)-1, 0, -1):
        if arr[x-1] > arr[x]:
            bump = x
            break

    min = arr[dip]
    min_index = dip
    for x in range(dip, bump):
        if arr[x] < min:
            min = arr[x]
            min_index = x

    for x in range(min_index, -1, -1):
        if arr[min_index] > arr[x]:
            min_index = x+1
            break

    return (min_index, bump)



print(find([1,3,5,2,6,4,7,8,9]))