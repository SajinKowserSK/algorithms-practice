import heapq

def swap(arr, i_1, i_2):
    tmp = arr[i_1]
    arr[i_1] = arr[i_2]
    arr[i_2] = tmp

    return arr

def lilysHomework(arr):

    asc_arr = sorted(arr)
    desc_arr = sorted(arr, reverse=True)

    asc_diffs = 0
    desc_diffs = 0
    for x in range(0, len(arr)):
        if arr[x] != asc_arr[x]:
            asc_diffs += 1

    for x in range(0, len(arr)):
        if arr[x] != desc_arr[x]:
            desc_diffs += 1

    # faster to swap towards ascending
    if asc_diffs <= desc_diffs:
        return min_heap_soln(arr)

    else:
        return max_heap_soln(arr)

def min_heap_soln(arr):
    heap = []

    for x in range(0, len(arr)):
        heapq.heappush(heap, (arr[x], x))

    swaps = 0
    for x in range(0, len(arr)):
        popped = heapq.heappop(heap)
        if popped[0] < arr[x]:
            swap(arr, popped[1], x)
            swaps += 1

    return swaps

def max_heap_soln(arr):
    heap = []

    for x in range(0, len(arr)):
        heapq.heappush(heap, (arr[x]*-1, x))

    swaps = 0
    for x in range(0, len(arr)):
        popped = heapq.heappop(heap)
        if abs(popped[0]) > arr[x]:
            swap(arr, popped[1], x)
            swaps += 1

    return swaps


# TEST CASE 1
# [2,1,4,5], swaps should be just (2,1) to get sorted ascending array so 1
# test = [2,1,4,5]

# TEST CASE 2
# [3,4,2,5,1], swaps should be (5,3) and then (2,3) to get sorted descending array so 2
# test = [3,4,2,5,1]

# have to uncomment test cases above
print(lilysHomework(test))