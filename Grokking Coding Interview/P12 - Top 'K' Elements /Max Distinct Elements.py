from heapq import *


def find_maximum_distinct_elements(nums, k):
    hmap = {}
    minHeap = []

    for elem in nums:
        if elem in hmap:
            hmap[elem] += 1

        else:
            hmap[elem] = 1

    distincts = 0
    for elem, freq in hmap.items():
        if freq == 1:
            distincts += 1

        else:
            heappush(minHeap, (freq, elem))


    while len(minHeap) > 0 and k > 0:
        popped = heappop(minHeap)
        popped = list(popped)

        while popped[0] != 1:
            popped[0] -= 1
            k-= 1

        if k >= 0:
            distincts += 1

    if k > 0:
        distincts -= k

    return distincts



def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

