class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        for x in range(0, len(s)):
            len1 = self.helper(s, x, x) # palindromes of len odd int
            len2 = self.helper(s, x, x + 1) # palindromes of len even int
            maxlen = max(len1, len2) # max of both

            if maxlen > (end - start): # if maxLen is longer than our current end - start
                start = x - int(((maxlen - 1) / 2)) # half of the max len goes to the left
                end = x + int(maxlen / 2) # half of the maax len goes to the right

        return s[start:end + 1]

    def helper(self, s, left, right):

        # as long as we are within boundaries and both sides reflect each other, expand outwards
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        # the reason why we need to add the -1 is because
        # racecar -> at last iteration we are at L = 0 aand R = 6
        # they are equal to each other so we dec left by 1 more and inc right by 1 more
        # typical formula to calculate len is R - L + 1
        # now L = -1 and R = 7 and typical R - L + 1 -> 7 - (-1) + 1 -> 9
        # we need to undo that last decrement
        # (R - 1) - (L + 1) + 1    -> 7 -1 - 0 + 1 -> 7
        return right - left - 1


