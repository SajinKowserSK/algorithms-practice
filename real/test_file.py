

def divisibility(s, t):
    new = s.replace(t, "")
    if len(new) != 0:
        return -1


    repeating_len = smallestWindow(t)
    return repeating_len


def smallestWindow(t):
    strLen = len(t)

    lowest = float("inf")
    for x in range(int(strLen/2), 0, -1): # start from mid bc we want it to repeat
        if strLen % x == 0:
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