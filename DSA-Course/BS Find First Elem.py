def find(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:

        mid = int((end+start)/2)

        if arr[mid] == target and (mid == 0 or mid > 0 and arr[mid-1] != target):
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1


    return -1


print(find([4,4,4,4,5,6], 4))

