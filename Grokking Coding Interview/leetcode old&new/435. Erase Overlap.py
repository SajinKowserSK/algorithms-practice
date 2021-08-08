class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[1])

        erase = 0

        x = 0

        while x < len(intervals) - 1:

            curr = intervals[x]
            nex = intervals[x + 1]

            if nex[0] < curr[1]:
                intervals.pop(x + 1)
                erase += 1
                x = 0
                continue

            x += 1

        return erase









