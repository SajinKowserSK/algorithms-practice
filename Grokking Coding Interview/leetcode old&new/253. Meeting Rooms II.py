import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

            # make heap
        # add start to heap
        # for intervals in heap
        # pop out the earliest
        # if the curr start is after or equal to earliest's end time
        # modify earliest's end time to be curr end time
        # otherwise add it to the heapq
        # return size of heapq

        intervals = sorted(intervals)

        heap = []
        heapq.heappush(heap, intervals[0][1])

        for x in range(1, len(intervals)):
            interval = intervals[x]
            popped = heapq.heappop(heap)

            if interval[0] >= popped:
                popped = interval[1]

            else:
                heapq.heappush(heap, interval[1])

            heapq.heappush(heap, popped)

        print(heap)
        return len(heap)