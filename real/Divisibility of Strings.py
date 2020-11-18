def find_pattern(s):
    i = (s+s).find(s, 1, -1)
    if i == -1:
        return None

    return s[:i]


def divisibility(str1, str2):
    return True if find_pattern(str1) == find_pattern(str2) else False


print(divisibility("bcdbcdbcdbcd", "bcdbcda"))



