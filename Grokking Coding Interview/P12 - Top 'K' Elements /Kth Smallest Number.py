from heapq import *

def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  minHeap = []

  for x in range(k):
      heappush(minHeap, nums[x])

  for x in range(k+1, len(nums)):
      if minHeap[-1] > nums[x]:
          minHeap.pop(-1)
          heappush(minHeap, nums[x])


  return list(minHeap)[-1]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
