class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        for x in range(0, len(s)):
            len1 = self.helper(s, x, x)
            len2 = self.helper(s, x, x + 1)
            maxlen = max(len1, len2)

            if maxlen > (end - start):
                start = x - int(((maxlen - 1) / 2))
                end = x + int(maxlen / 2)

        return s[start:end + 1]

    def helper(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        return right - left - 1


