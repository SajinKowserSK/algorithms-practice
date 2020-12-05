# then check for smallest repeating substring -> O(Factors(N) * (N/Factor(N)) -> O(N*M) since they don't reduce

def divisibility(s, t):
    if len(s) % len(t) != 0:
        return -1


    repeating_len = smallestWindow(t)
    repeating_len2 = smallestWindow(s)
    return repeating_len if repeating_len == repeating_len2 else -1


# "abab" -> 2 since "ab" is smallest window that repeats
# "abcabc" -> 3 since "abc" is smallest
def smallestWindow(t):
    strLen = len(t)

    lowest = float("inf")
    for x in range(int(strLen/2), 0, -1): # start from mid bc we want it to repeat atleast twice
        if strLen % x == 0: # only consider indices so that total len is divisble evenly by index
            repeats = int(strLen / x)
            curr_substr = t[0:x]

            new_str = ""
            for y in range(0, repeats):
                new_str += curr_substr

            if new_str == t:
                lowest = len(curr_substr)

    return lowest




s = "ababababab"
t = "abab"

print(divisibility(s, t))

def find_pattern(s):
    i = (s+s).find(s, 1, -1)
    if i == -1:
        return None

    return s[:i]


def divisibility(str1, str2):
    return True if find_pattern(str1) == find_pattern(str2) else False


print(divisibility("bcdbcdbcdbcd", "bcdbcda"))



