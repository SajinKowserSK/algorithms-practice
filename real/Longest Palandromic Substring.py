# O(n^2) optimized soln
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


