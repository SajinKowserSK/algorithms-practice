# Given an array of integers, find the shortest sub array, that if sorted, results in the
# entire array being sorted.For example:[1,2,4,5,3,5,6,7] --> [4,5,3] - If you sort from indices 2 to 4,
# the entire array is sorted.[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] -
# If you sort from indices 1 to 5, the entire array is sorted.
# Questions to Clarify:Q. How to return the result?A. Return the result as a pair of indices.

def sortedSubArray(arr):

    if len(arr) == 0 or len(arr) == 1:
        return None

    # find the first dip in values (goes down instead of up)
    # must initialize outside of function header to reduce off by 1 error
    start = 0
    for x in range (start, len(arr)-1):
        if arr[start+1] < arr[start]:
            break

        start = start + 1

    # if it equals the length - 1 then that means no dips, return None

    if start == len(arr)-1:
        return None

    # find bumps by traversing from back
    for end in range (len(arr)-1, -1, -1):
        if arr[end-1] > arr[end]:
            break

     # now we have the start and end indices for dip and bump, must get
     # must get min and max of the sub array and see if theres anything else in the WHOLE
     # array that is smaller or larger than these min and maxes (to ensure whole thing is sorted correctly)

    # default vals since they're sorted
    minVal = arr[start]
    maxVal = arr[end]

    # gets sub array's min and max
    for x in range (start, end+1):
        currElem = arr[x]
        minVal = min(minVal, currElem)
        maxVal = max(maxVal, currElem)

    # traverse left to expand array to include elements shorter than min

    for x in range (start, 0, -1):
        if arr[x-1] <= minVal:
            break

        start = start - 1

    for x in range (end, len(arr)-1):
        if arr[x+1] >= maxVal:
            break

        end = end + 1

    return "(" + str(start) +", " + str(end) + ")"


print(sortedSubArray([1,2,4,5,3,5,6,7]))
print(sortedSubArray([1,3,5,2,6,4,7,8,9]))



