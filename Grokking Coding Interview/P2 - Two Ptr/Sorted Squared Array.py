class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1

        aux = []

        while start <= end:
            right = nums[end] * nums[end]
            left = nums[start] * nums[start]

            if right >= left:
                aux.append(right)
                end -= 1

            else:
                aux.append(left)
                start += 1

        aux = aux[::-1]
        return aux



