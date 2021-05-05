class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add interval to list
        # sort it by start time

        # make a new list and add all the times
        # check for overlaps between last added item in new list and the to be added items
        # merge where necessary

        intervals.append(newInterval)
        intervals.sort()
        newL = []
        newL.append(intervals[0])

        for x in range(1, len(intervals)):
            curr = intervals[x]
            if newL[-1][1] >= curr[0] or curr[0] <= newL[-1][0]:
                newL[-1] = [min(newL[-1][0], curr[0]), max(newL[-1][1], curr[1])]

            else:
                newL.append(curr)

        return newL



