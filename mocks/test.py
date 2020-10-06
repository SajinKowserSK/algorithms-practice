import heapq

def swap(arr, i_1, i_2):
    tmp = arr[i_1]
    arr[i_1] = arr[i_2]
    arr[i_2] = tmp

    return arr

def lilysHomework(arr):
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


print(lilysHomework([2,5,3,1]))