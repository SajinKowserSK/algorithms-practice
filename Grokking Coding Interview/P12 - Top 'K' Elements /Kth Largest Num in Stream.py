from heapq import *

class KthLargestNumberInStream:
  minHeap = []
  def __init__(self, nums, k):
    # TODO: Write your code here
    self.k = k
    for num in nums:
      self.add(num)

  def add(self, num):
    heappush(self.minHeap, num)

    if len(self.minHeap) > self.k:
      heappop(self.minHeap)


    return self.minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

