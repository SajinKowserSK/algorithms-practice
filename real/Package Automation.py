import heapq


def automate(numGroups, arr):
    min_heap = []
    heapq.heapify(min_heap)

    for elem in arr:
        heapq.heappush(min_heap, elem)

    output = [1]

    while len(output) < numGroups:
        popped = heapq.heappop(min_heap)
        if popped >= output[-1] + 1:
            popped = output[-1] + 1 # reduce gt or eq number to highest possible num

        else:
            popped = output[-1] # we know there are min 1 items in each group, so at we can always reduce to output[-1]

        output.append(popped)

    # because we filled first one with 1, we know there's always an extra group
    # if the extra group is greater than our last elem AND
    # LAST ELEM and SECOND LAST ELEM are the same, then we can increment last elem by one
    final_elem = heapq.heappop(min_heap)

    if final_elem >= output[-1] + 1:
        output[-1] = output[-1] + 1

    return output[-1]


testcases = [[1,3,2,2], [3,2,3,5], [1,1,1,5],
             [2,2,3,4], [1,1,1,1]]

for test in testcases:
    print(automate(len(test), test))