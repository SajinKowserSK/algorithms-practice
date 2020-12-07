# find closest number to target
# identical to BS, just keep track of the abs(closest_difference) to the target
# if target is in array return target
# return as pos index

def closestElement(arr, target):
    if arr is None or len(arr) == 0:
        return None

    start = 0
    end = len(arr)-1
    closest = None
    closest_pos = None

    while start <= end:
        mid = start + (end - start)/2
        mid = int(mid)

        currentDistance = abs(arr[mid]-target)

        if closest is None or currentDistance < closest:
            closest = currentDistance
            closest_pos = mid

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return closest_pos

test = [2,3,5,8,9,11]
test2 = [2,6,12,34]
test3 = [1,5,7,12]
print(closestElement(test, 7))