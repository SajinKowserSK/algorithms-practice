# brute force soln -> O(n * m) where m is size of sliding window, O(1) space
def analysis(numComputer, hardDiskSpace, segmentLength):
    max_val = float("-inf")
    start = 0

    while (start + segmentLength) <= numComputer:

        minima = float("inf")

        for x in range(start, start+segmentLength):
            curr = hardDiskSpace[x]
            minima = min(curr, minima)

        max_val = max(minima, max_val)
        start += 1

    return max_val

# optimized soln -> O(n) TC and O(n) SC
def analysis2(numComputer, hardDiskSpace, segmentLength):
    max_minima = float("-inf")
    i = 0
    dq = [] # stores indices, with the first being the most min val and the last being the max val
    # dq holds items in ascending order, dq[0] will give us min for the subarray, and dq[-1] would give us max
    while i < numComputer:
        curr_elem = hardDiskSpace[i]
        start_window = i - segmentLength + 1

        if dq and dq[0] < start_window:
            dq.pop(0)

        # now that we have a valid dq range we need to add the current elem to update the dq's mins and maxs
        # because we want min at the start, max at the bottom, we pop all elems right to left so long as
        # curr_elem < dq[-1]

        while dq and curr_elem < hardDiskSpace[dq[-1]]:
            dq.pop(-1)

        dq.append(i)

        # now we can access the window's minima by doing dq[0]
        # but we only want to do this if we've processed atleast segmentLen elems

        if i >= segmentLength -1:
            curr_window_min = hardDiskSpace[dq[0]]
            max_minima = max(max_minima, curr_window_min)

        i += 1

    return max_minima





hardDiskSpace = [8,2,4,3]
numComputer = len(hardDiskSpace)
segLen = 2

print(analysis(numComputer, hardDiskSpace, segLen))
print(analysis2(numComputer, hardDiskSpace, segLen))


