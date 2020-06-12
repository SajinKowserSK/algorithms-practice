# given cyclically sorted array, find min in logarithmic time
# [7,8,1,2,4,6]  = 1 so return pos 2
# [5,6,7,1] = 1 so return 4
# [1,2,3,4] = 1 so return 0



# Approach
# We know bc its cyclically sorted, min element will be less than left neighbour
# by default it is also less than right neighbour, dont check for this
# Get the right most element

# Compare it to mid. If arr mid is > rightmost, you know that everything to the right will be
# bigger than right most so rightmost is smaller or something between arr mid and right is smallest

# If arr mid < rightmost then you know that everything after right (left of mid) will be bigger
# than the right unless the arr starts to the left. At same time, you know from mid to right, will be numbers > mid
# means either mid is the min (check if < left neighbour)
# or end = mid - 1 (go left)

def findMin(arr):
    if arr is None or len(arr) == 0:
        return None

    start = 0
    end = len(arr)-1
    rightm = arr[end]

    while start <= end:
        mid = start + (end - start)/2
        mid = int(mid)

        if arr[mid] > rightm:
            # go right, either rightm is lowest or something in between
            start = mid + 1

        elif arr[mid] < rightm and mid == 0 or arr[mid-1] > arr[mid]:
            # if less than rightm, everything in between will be greater than mid
            # either check if mid is the lowest or go left
            return mid
        else:
            end = mid - 1 # goes left


    return mid


print(findMin([7,8,1,2,4,6]))