from heapq import *

def find_k_largest_numbers(nums, k):

  minHeap = []

  for x in range(0, k):
      heappush(minHeap, nums[x])

  for x in range(k, len(nums)):
      if nums[x] > minHeap[0]:
          heappop(minHeap)
          heappush(minHeap, nums[x])

  return list(minHeap)


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
