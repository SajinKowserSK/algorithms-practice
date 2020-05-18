# Technique: Kadane's Algorithm
# Level: Medium Given an array of integers that can be both +ve and -ve
# 'find the contiguous subarraywith the largest sum.' \
# For example:  [1,2,-1,2,-3,2,-5]  -> first 4 elements have the largest sum. Return (0,3)
# empty arrays not accepted

def pair(x, y):
    return ("("+str(x)+", "+str(y)+")")

def arrange(arr):
    result = arr[0]
    maxUpToThisIndex = arr[0]
    start = 0
    end = 0

    for x in range (1, len(arr)):
        currElem = arr[x]

        if currElem > maxUpToThisIndex + currElem:
            start = x

        maxUpToThisIndex = max(currElem, currElem + maxUpToThisIndex)

        result = max(maxUpToThisIndex, result)

    sum = 0
    for x in range (start, len(arr)):

        currElem = arr[x]
        sum = sum + currElem

        if sum == result:
            end = x

    return pair(start,end)

print(arrange([-2,-3,4,-1,-2,1,5,-3]))

