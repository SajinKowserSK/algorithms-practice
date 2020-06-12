class Solution(object):
    def lengthOfLastWord(self, s):
        list2 = s.split()

        if len(list2) == 0:
            return 0

        else:

            ret = len(list2[-1])
            return ret

