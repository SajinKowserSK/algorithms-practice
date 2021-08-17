from heapq import *


class MedianOfAStream:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

        # seperate the stream to two diff parts, those less than the median and those more

    # I am interested in the highest for those less and the lowest for those more
    # if even I will take avg of top two elems and if odd, I will store the extra node in the minHeap
    # if odd elems inserted, I will store extra in the minheap and the root will be the median
    # if even elems inserted, I will store it in maxHeap and the avg of two roots of heaps will be median

    # at all times the diff between the two heaps' length cannot be greater than 1
    # this is because if we evenly seperated a list from the middle, no side would have > 1 element diff

    # as such, since we are storing the extra elem in the minheap (elems greater than the median), the condition
    # for every incoming number is to check if it is less than the root of the minheap or not

    # heapq heappush by default puts it in ascending order so for the maxHeap have to push -1 * num
    def insert_num(self, num):
        if len(self.minHeap) == 0 or num >= self.minHeap[0]:
            heappush(self.minHeap, num)

        else:
            heappush(self.maxHeap, -num)

        if len(self.minHeap) > len(
                self.maxHeap) + 1:  # the minHeap has too many items, must balance by rmeoving 1 node and sending to other heap
            heappush(self.maxHeap, -heappop(self.minHeap))

        elif len(self.minHeap) < len(self.maxHeap):  # we decided earlier that the minheap should have more items
            heappush(self.minHeap, -heappop(
                self.maxHeap))  # all nums in maxHeap were negs bc of heapq's minheap default push settings

        print("minheap", self.minHeap, "maxheap", self.maxHeap)

    def find_median(self):
        print(self.minHeap)
        print(self.maxHeap)
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2

        else:
            return self.minHeap[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(1)
    medianOfAStream.insert_num(2)
    medianOfAStream.insert_num(7)
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(6)
    medianOfAStream.insert_num(7)

    print("The median is: " + str(medianOfAStream.find_median()))


main()
