class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if palindrome is None or len(palindrome) == 1:
            return ""

        pal = list(palindrome)
        left = 0
        right = len(palindrome) - 1

        while left < right:  # can't be equal to then all a's and palindrome
            if pal[left] != "a":  # given valid palindrome so right is also equal to a
                pal[left] = "a"
                return "".join(pal)

            left += 1
            right -= 1

        # everything is an a
        pal[-1] = "b"
        return "".join(pal)