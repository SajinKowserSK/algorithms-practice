from helpers import *

def longest(arr):
    start = 0
    end = 0
    finStart = 0
    finEnd = 0
    myMap = {}

    while end < len(arr):
        if start > end:
            start = end
            end = end + 1

        else:
            nextItem = arr[end]

            if nextItem not in myMap:
                myMap[nextItem] = end
                end = end + 1

            else:
                # recall that we updated end to be the next item
                # (so up to end-1 is unique)

                if end-1-start+1 > finEnd - finStart + 1:
                    finStart = start
                    finEnd = end-1

                del myMap[arr[start]]
                start = start + 1

        # check for in case substring is start to the end of the array
        if end - 1 - start + 1 > finEnd - finStart + 1:
            finStart = start
            finEnd = end - 1


    return pair(finStart, finEnd)


def substring2(arr):
    start = 0
    end = 0
    longest = 1
    result = [0,0]
    myMap = {}

    while end < len(arr)-1:
        end += 1
        ch = arr[end]

        if ch in myMap and myMap[ch] >= start:
            start = myMap[ch] + 1

        myMap[ch] = end

        if end - start + 1 > longest:
            longest = end - start + 1
            result[0] = start
            result[1] = end

    return result

test = chArr("sajapgjyzt")
print(longest(test))
print(substring2(test))