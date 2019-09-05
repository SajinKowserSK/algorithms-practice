class Solution(object):
    def intersect(self, nums1, nums2):
        retList = []
        same = []

        counter = 0

        for x in nums1:

            for y in nums2:

                if x == y and x not in same:
                    same.append(x)

        for x in same:
            nums1_counter = 0
            nums2_counter = 0

            for t in nums1:
                if x == t:
                    nums1_counter = nums1_counter + 1

            for c in nums2:
                if x == c:
                    nums2_counter = nums2_counter + 1

            smaller = min(nums1_counter, nums2_counter)

            retList.extend(x for i in range(smaller))

        return retList

