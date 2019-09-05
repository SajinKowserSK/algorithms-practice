class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        sorNums = nums[:]
        sorNums.sort()
        for x in range(0, len(sorNums) - 1):
            if sorNums[x + 1] == sorNums[x]:
                indices = [i for i, y in enumerate(nums) if y == sorNums[x]]
                indices.sort()
                for e in range(0, len(indices) - 1):
                    if abs(indices[e] - indices[e + 1]) <= k:
                        return True

        return False

