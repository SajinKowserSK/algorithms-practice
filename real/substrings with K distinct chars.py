def distinct(s, k):
    k_distinct = helper(s, k)
    k_distinct_less = helper(s, k-1)

    return k_distinct - k_distinct_less

def helper(s, k):
    if k == 0:
        return 0

    total = 0
    map1 = {}
    left = 0
    diff = 0

    for char in s:
        map1[char] = 0

    for right in range(0, len(s)):
        curr = s[right]

        if map1[curr] == 0:
            diff += 1

        map1[curr] += 1

        if diff <= k:
            total += right - left + 1

        else:
            while left <= right and left < len(s) and diff > k:
                left_val = s[left]
                map1[left_val] -= 1

                if map1[left_val] == 0:
                    diff -= 1

                left += 1

            total += right - left + 1

    return total


print(distinct("aabab", 3))


