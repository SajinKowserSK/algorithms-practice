# given sorted array of unknown length (imagine blank spots are -1) find target

def findTarget(arr, target):
    if len(arr) == 0 or arr is None:
        return None

    start = 0
    end = 1

    while True:
        end = end * 2
        tmp = arr[end]



        if tmp is None:
            endPoint = binSearchOverRange(arr, end/2, end)

            break

    return binarySearch(arr, start, endPoint, target)


def binSearchOverRange(arr, low, high):
    while low <= high:
        mid = int(low + (high - low) / 2 )


        if arr[mid] is None:
            high = mid - 1

        else:
            if arr[mid+1] is None:
                return mid

            else:
                low = mid + 1

    return None

def binarySearch(arr, start, endPoint, target):


    while start <= endPoint:
        mid = int(start + (endPoint - start) / 2)

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            endPoint = mid - 1

        else:
            start = mid + 1

    return None

test = [1,2,6,9,11,33,None,None,None,None]
print(findTarget(test, 1))










