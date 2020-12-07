import heapq

# we know that items in group are always >= 1
# we know that larger items can be REDUCED to smaller items
# we know 0 <= arr[i] - arr[i - 1] < 1 since all items are > 1 and can only be bigger than prev by 1

# first item has to be == 1
# for all following item we can do a greedy approach -> if the next smallest item is >= prev + 1
# we reduce it to the biggest possible number which is prev + 1
# since this is a min heap we know that all numbers after this can also be reduced to prev + 1 so we are safe

# if a next smallest number is <= prev
# we know that the prev is always 1. <= 1 at the worst case is going to be 1 since the smallest items in group is 1
# so we say if popped is NOT >= prev + 1, simply leave popped as popped or popped  = prev

# in the end we will have 1 item left in heap since we added an extra "1" as our first elem
# if this item is > our current last elem in the final output array, we know that the maximum final element
# is going to be final[-1] + 1 since we just made one non optimal switch as a result of making n-1 choices.

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
    # if the extra group is greater than our last elem
    final_elem = heapq.heappop(min_heap)

    if final_elem >= output[-1] + 1:
        output[-1] = output[-1] + 1

    return output[-1]


testcases = [[1,3,2,2], [3,2,3,5], [1,1,1,5],
             [2,2,3,4], [1,1,1,1]]

for test in testcases:
    print(automate(len(test), test))