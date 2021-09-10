from heapq import *
def find_Kth_smallest(lists, k):
  number = -1
  res = []
  minHeap = []

  for lst in lists:
    heappush(minHeap, lst)

  while minHeap and len(res) < k:
    popped = heappop(minHeap)
    res.append(popped[0])
    popped.pop(0)
    heappush(minHeap, popped)

  return res[-1]


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
