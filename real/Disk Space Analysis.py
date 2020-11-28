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


hardDiskSpace = [8,2,4]
numComputer = len(hardDiskSpace)
segLen = 2

print(analysis(numComputer, hardDiskSpace, segLen))


