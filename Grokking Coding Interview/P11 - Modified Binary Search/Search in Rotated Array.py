class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxI = self.findMax(nums)
        left = self.bs(0, maxI, nums, target)
        right = self.bs(maxI + 1, len(nums) - 1, nums, target)

        return max(-1, left, right)

    def findMax(self, arr):
        start, end = 0, len(arr) - 1
        LM = arr[0]

        while start < end:
            mid = start + (end - start) / 2
            mid = int(mid)

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid] < LM:
                end = mid - 1

            else:
                start = mid + 1

        return start

    def bs(self, start, end, arr, target):
        while start <= end:
            mid = start + (end - start) / 2
            mid = int(mid)

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return -1
"" \
""