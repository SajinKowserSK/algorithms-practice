# Given an array ARR
# AND VALUE K
# return the number of sub arrays that can be returned with K ODD VALUES

def subArrayHasKOddNumbers(subarray,k):
    """Return the subarray has exact k odd numbers."""

    oddCounter = 0

    for items in subarray:
        if items % 2 != 0:
            oddCounter += 1

    return oddCounter == k
def satisfyingSubarrays(arr, k):
    subArrays =[]

    for x in range(len(arr)):
        for y in range(len(arr), x, -1):
            if len(arr[x:y]) >= k:
                if subArrayHasKOddNumbers(arr[x:y],k):
                    subArrays.append(arr[x:y])

    return len(subArrays)
