# O(n^2) optimized soln
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # longest palindrome indice starts at first char
        start = 0
        end = 0

        for x in range(0, len(s)):
            # do both versions, one where there is a definitive mid and one for where there can be two mids
            len1 = self.helper(s, x, x)
            len2 = self.helper(s, x, x + 1)
            maxlen = max(len1, len2)

            # only if maxlen is greater than our current end - start len
            if maxlen > (end - start):
                # x - (maxLen-1) / 2
                # Minus bc going left -> maxLen -1 because want the left side of maxLen/2
                start = x - int(((maxlen - 1) / 2))

                # same logic, don't need maxLen + 1 this time
                end = x + int(maxlen / 2)

        return s[start:end + 1]

    def helper(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        # R - L + 1 will give you 9 for racecar instead of 7
        return right - left - 1




    # O(n^3) soln
class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = []

        lst = list(s)

        for x in range(0, len(s)):
            left = s[x]

            for y in range(x, len(s)):
                right = s[x]

                if left == right:
                    front_sub = lst[x:y + 1]
                    back_sub = front_sub[::-1]

                    front_sub_str = "".join(front_sub)
                    back_sub_str = "".join(back_sub)

                    if front_sub_str == back_sub_str and (len(ans) == 0 or len(front_sub) > ans[0]):
                        print(front_sub_str, back_sub_str)
                        ans = [len(front_sub), "".join(front_sub)]

        return ans[1]


