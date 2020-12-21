def main(arr, target):
    start = find_earliest(arr, target)
    end = find_latest(arr, target)
    return list((start, end))

def find_earliest(arr, target):
    if arr == None:
        return -1

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = int((start+end)/2)
        if arr[mid] == target and (mid == 0 or mid > 0 and arr[mid-1] != arr[mid]):
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


def find_latest(arr, target):
    if arr == None:
        return -1

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target and (mid == end or mid < end and arr[mid + 1] != arr[mid]):
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return -1


print(main([2,2,2,2,2], 2))