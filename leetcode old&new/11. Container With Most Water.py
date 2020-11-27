class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_num = 0

        start = 0
        end = len(height) - 1

        while start < end:
            start_elem = height[start]
            end_elem = height[end]

            vertical = min(start_elem, end_elem)
            horizontal = end - start

            max_num = max(max_num, vertical * horizontal)

            if start_elem > end_elem:
                end -= 1

            else:
                start += 1

        return max_num
