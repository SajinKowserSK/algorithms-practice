# Level: Easy
# Given an array of integers, rearrange the elements such that all zeros aremoved to the end of the array

def move(arr):

    if len(arr) == 0:
        return arr

    zeroSpot = len(arr)-1

    while zeroSpot > 0 and arr[zeroSpot] == 0:
        zeroSpot = zeroSpot - 1

    if zeroSpot == 0:
        return arr

    i = zeroSpot - 1

    while i != -1:
        if arr[i] == 0:
            tmp = arr[zeroSpot]
            arr[zeroSpot] = arr[i]
            arr[i] = tmp
            zeroSpot = zeroSpot - 1

        i = i - 1
    return arr

def move2(arr):
    boundary = 0
    for x in range (0, len(arr)):
        if (arr[x] == 0):
            tmp = arr[boundary]
            arr[boundary] = arr[x]
            arr[x] = tmp

            boundary = boundary + 1
    return arr

print(move([4,2,0,1,0,3,0]))
print(move2([4,2,0,1,0,3,0]))