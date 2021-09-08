from heapq import *

def find_k_frequent_numbers(nums, k):
  topNumbers = []
  hmap = {}
  minHeap = []

  for elem in nums:
      if elem not in hmap:
          hmap[elem] = 1

      else:
          hmap[elem] += 1

  for num, freq in hmap.items():
      heappush(minHeap, (freq, num))
      if len(minHeap) > k:
          heappop(minHeap)

  while minHeap:
      topNumbers.append(heappop(minHeap)[1])

  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

