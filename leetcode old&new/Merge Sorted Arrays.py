class Solution(object):

    def merge(self, nums1, m, nums2, n):

        place = len(nums1) - 1
        nums1ptr = m - 1
        nums2ptr = n - 1

        while nums2ptr > -1 and nums1ptr > -1:

            if nums2[nums2ptr] > nums1[nums1ptr]:
                nums1[place] = nums2[nums2ptr]
                nums2ptr -= 1

            else:
                nums1[place] = nums1[nums1ptr]
                nums1ptr -= 1

            place = place - 1

        if nums1ptr <= 0:
            while place > -1 and nums2ptr != -1:
                nums1[place] = nums2[nums2ptr]
                nums2ptr = nums2ptr - 1
                place = place - 1

        if nums2ptr <= 0:
            while place > -1 and nums1ptr != -1:
                nums1[place] = nums1[nums1ptr]
                nums1ptr -= 1
                place = place - 1 



