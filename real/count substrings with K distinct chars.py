# to find all the combinations of K size, we can take the combinations of K and K -1's difference
def distinct(s, k):
    k_distinct = helper(s, k)
    k_distinct_less = helper(s, k-1)

    return k_distinct - k_distinct_less

def helper(s, k):
    if k == 0:
        return 0

# start a total, char map, left and diff
    total = 0
    map1 = {}
    left = 0
    diff = 0

    for char in s:
        map1[char] = 0

# as the "right" ptr approaches the Nth element
    for right in range(0, len(s)):
        curr = s[right]

        # increment occurences of characters in the map and different elements as well if appropriate

        if map1[curr] == 0:
            diff += 1

        map1[curr] += 1

        # CASE 1 -> diff is less than equal to K -> we can count this combination by R - L + 1
        if diff <= k:
            total += right - left + 1

        # CASE 2 -> if diff > k we need to bring diff down to k
        else:

            # left <= right and left < len(s) for AOB prevention
            # continously close the indices windows in, check if after closing in the index, the occurence turns to 0
            # if it turns to 0 then we know we have 1 less diff element

            while left <= right and left < len(s) and diff > k:
                left_val = s[left]
                map1[left_val] -= 1

                if map1[left_val] == 0:
                    diff -= 1

                left += 1

            # once we have successfully updated left ptr such that there are K distinct elems in the window
            # we can get the combinations with R - L + 1
            total += right - left + 1

    return total


print(distinct("aabab", 3))


