def main(root):
    maxVal = float("-inf")
    helper(root, maxVal)
    return maxVal[0]


def helper(root, maxVal):
    if root is None:
        return (0, 0) # represents avg as index 0 and then len as index 1

    nbrs = root.children

    currTotal = root.val
    currLen = 1
    for nbr in nbrs:
        curr = helper(nbr, maxVal)
        currTotal += curr[0] * curr[1] # get avg * len to get total
        currLen += curr[1]

    avg = currTotal / currLen

    if currLen > 1 and avg > maxVal[0]:
        maxVal[0] = avg

    return (avg, currLen)