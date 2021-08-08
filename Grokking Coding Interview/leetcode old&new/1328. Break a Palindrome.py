class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # if a string is len 1 then no matter what we replace, it will be palindrome (read sameway both ways)
        if len(palindrome) == 1:
            return ""
        # LST bc strings immutable in python
        lst = list(palindrome)
        start = 0
        end = len(palindrome) - 1

        # since we are guaranteed palindromic string, we know string[start] always == string[end]
        while start <= end:

            # if start isn't an a and we are still before the mid point -> break
            # we can replace that w/ midpoint
            if lst[start] == "a":
                start += 1
                end -= 1

            else:
                break

        # if start < end then we know that before midpoint we can replace start w/ an a
        if start < end:

            lst[start] = "a"
            return "".join(lst)

        # means all the strings were a's so we can just change the last char to a "b"
        else:
            lst[-1] = "b"
            return "".join(lst)




