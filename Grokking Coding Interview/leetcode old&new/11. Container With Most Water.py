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


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_size = float('-inf')
        while start < end:
            left = height[start]
            right = height[end]

            min_h = min(left, right)
            width = end - start

            area = min_h * width

            max_size = max(max_size, area)

            if left < right:
                start += 1

            else:
                end -= 1

        return max_size

