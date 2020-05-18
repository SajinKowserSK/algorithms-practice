# Level: Easy You are given an array of integers.
# Rearrange the array so that all zeroes are atthe beginning of the array.
# For example,a = [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]

def move(arr):
    if len(arr) == 0:
        return arr

    zeroSpot = 0
    while zeroSpot < len(arr) and arr[zeroSpot] == 0:
        zeroSpot = zeroSpot + 1

    if zeroSpot == len(arr)-1:
        return arr

    i = zeroSpot + 1
    while i < len(arr):
        if arr[i] == 0:
            tmp = arr[zeroSpot]
            arr[zeroSpot] = arr[i]
            arr[i] = tmp
            zeroSpot = zeroSpot + 1

        i = i + 1
    return arr
print(move([4,2,0,1,0,3,0]))