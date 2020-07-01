from helpers import *

def subArr(arr, target):
    start = 0
    end = 0
    currSum = arr[start]

    while end <= len(arr)-1:
        if start > end:
            start = end
            end = end + 1

        else:
            if currSum == target:
                return pair(start, end)

            elif currSum < target:
                end = end + 1
                try:
                    currSum += arr[end]

                except:
                    pass
            else:
                currSum -= arr[start]
                start = start + 1

    return None



print(subArr([4,6,3,1,0], 14))