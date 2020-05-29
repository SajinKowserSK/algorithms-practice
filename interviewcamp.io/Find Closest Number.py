# 1. (Level: Easy)
# Given a sorted array A and a target T, find the target. If the target is not in the array, find the number closest to the target.
# For example, if A = [2,3,5,8,9,11] and T = 7, return 8.
# Technique: Binary Search Record and Move On

def findClosest(arr, target):
    if arr == None or target == None or len(arr) ==0:
        return None

    start = 0
    end = len(arr)-1
    result = None
    returnPos = None

    while (start <= end):
        # to prevent integer overflow
        mid = start + (end-start)/2
        mid = int(mid) # to prevent indexing float

        if (result == None or abs(target-arr[mid]) < result):
            result = abs(target-arr[mid])
            returnPos = mid


        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return returnPos


sajin = findClosest([2,3,5,8,9,11], 7)
print(sajin)

