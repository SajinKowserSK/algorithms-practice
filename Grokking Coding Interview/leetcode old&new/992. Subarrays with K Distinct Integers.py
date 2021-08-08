class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        # we can calculate K distinct by getting difference between
        # all subarrays with 1 to K inclusive subarrays and
        # all subarrays with 1 to K-1 inclusive subarrays
        # doing so will leave us with just K distinct subarrays

        k_distinct = self.helper(A, K)
        k_distinct_less = self.helper(A, K - 1)

        print(k_distinct, k_distinct_less)
        return k_distinct - k_distinct_less

    def helper(self, A, K):

        # break case, we know that if K= 0, we return 0 since subarrays with 0 distinct
        # elems is not possible

        if K == 0:
            return 0

            # create a map that holds occurence of each array's unique values
        # with respect to the length of our current subarray
        map1 = {}

        count = 0
        diff = 0
        left = 0

        # set every occurence to 0
        for elem in A:
            map1[elem] = 0

            # iterate through with X being the "rightmost" end
        for x in range(0, len(A)):
            curr = A[x]

            # if we encounter an array value that we haven't seen yet in our subarray
            # increase the number of diff
            if map1[curr] == 0:
                diff += 1

                # increase at each occurence
            map1[curr] += 1

            # As long as the difference is less than or equal to K
            # we continue to increment count by all the subarrays between right and left
            if diff <= K:
                count += x - left + 1

            else:
                # if we have more than K diff, we need to close in our window from
                # the left side
                while left < len(A) and left <= x and diff > K:
                    # first decrease the occurence
                    map1[A[left]] -= 1
                    # if after decrease, the occurence is 0, we removed a unique val from subarray
                    # reduce diff
                    if map1[A[left]] == 0:
                        diff -= 1

                        # move left marker forward
                    left += 1

                    # need to again increment by all subarrays between right and left
                count += x - left + 1

        return count



