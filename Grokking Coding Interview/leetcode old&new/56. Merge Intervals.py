class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []

        intervals = sorted(intervals)
        final = []

        for interval in intervals:

            if len(final) == 0 or final[-1][1] < interval[0]:
                final.append(interval)

            else:
                final[-1][1] = max(final[-1][1], interval[1])

        return final



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []

        intervals = sorted(intervals)
        x = 0
        while x < len(intervals) - 1:

            curr_pair = intervals[x]
            next_pair = intervals[x + 1]

            if next_pair[0] >= curr_pair[0] and next_pair[0] <= curr_pair[1]:
                new_first = curr_pair[0]
                new_end = max(curr_pair[1], next_pair[1])

                intervals.pop(x)
                intervals.pop(x)
                intervals.insert(x, [new_first, new_end])

                x = 0
                continue

            x += 1

        return intervals

