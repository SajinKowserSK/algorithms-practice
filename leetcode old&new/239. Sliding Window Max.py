class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        dq = []  # will store indices
        i = 0

        while i < len(nums):
            curr_start = i - k + 1
            curr_elem = nums[i]

            if dq and dq[0] < curr_start:
                # if indice of max dq is before the rng of this
                # current window of size k

                dq.pop(0)

            # adding elem we have to ensure all elems before it are cut
            while dq and curr_elem > nums[dq[-1]]:
                dq.pop(-1)

            dq.append(i)

            window_max = nums[dq[0]]

            if i >= k - 1:
                output.append(window_max)

            i += 1

        return output