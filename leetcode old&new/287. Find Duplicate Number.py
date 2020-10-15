class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # need to find intersection point so we can have a ptr there
        while True:
            # need fast to go 2x speed of slow
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

                # start slow from start and keep fast at intersection
        # move both by 1 each time so they find their duplicate

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
