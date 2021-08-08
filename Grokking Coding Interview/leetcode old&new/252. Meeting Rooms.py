class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """

        if len(intervals) == 0:
            return True

        intervals.sort()

        for x in range(0, len(intervals) - 1):
            curr = intervals[x]
            nex = intervals[x + 1]

            if nex[0] < curr[1]:
                return False

        return True

