def subArrTarget(arr, target):


    if arr is None or len(arr) == 0:
        return None

    sum = 0
    myMap = {}

    for x in range(0, len(arr)):

        sum = sum + arr[x]

        if sum == target:
            return [0, x]

        # we want to find the subarray where our subarray INCREASED by TARGET amount
        # get that increase we do curr_sum - target
        # if that curr_sum - target is in the map then we know from that index
        # to current index, we have INCREASED by that number
        # so we can take the array from that index +1 to i
        if sum - target in myMap:
            return [myMap[sum - target] + 1, x]

        myMap[sum] = x

        print("SUM IS", sum, myMap)

    return None

test = [3,-1,2,4]
print(subArrTarget(test, 1))


