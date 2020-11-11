def least_greater(arr, k):
    if len(arr) == 0:
        return None

    start = 0
    end = len(arr) - 1

    min_num = None

    while start <= end:
        mid = int((start + end) / 2)
        curr_point = arr[mid]  # 6

        if curr_point == k:
            return curr_point

        elif curr_point < k:
            start = mid + 1

        else:  # curr_point > k
            min_num = curr_point
            end = mid - 1

    return min_num


tests = [[1, 2, 4, 5, 8],
         [1, 2, 3, 4, 5, 6],
         [8, 9, 10],
         [1, 1, 1, 1],
         []]

for case in tests:
    print(least_greater(case, 7))

print(least_greater([2, 3, 4, 5, 6], 1))  # 2

# ascending ord# we have a k
# one where some less and some more
# one where al lless
# all more
# empty list
# all of the same


# start here.

# print(overlap([[1,3],[8,10],[15,18],[2,6]])) # [[1,6],
# -> [[1,6]]

# one_away(s1, s2) -> whether one string is 'one away' from another string. What one away means is that s1 can be made into s2 or s2 can be made into s1 through one of three ops : add a character, replacing a character


("ab",
 "abc")  # one away because you can make s1 into s2 by adding a character. And also u can make abc -> ab by removing a character.


def one_way(s1, s2):
    # EDGE CASES -> duplicate chars
    # ensures s1 len is smaller than s2
    if len(s1) > len(s2):
        tmp = s2
        s2 = s1
        s1 = tmp

    s1_list = list(s1)
    s2_list = list(s2)

    diff = len(s2_list) - len(s1_list)

    if diff > 1:
        return False

    if diff == 0:
        # replace

        swapped = False
        for x in range(0, len(s1_list)):

            if s1_list[x] != s2_list[x] and swapped == True:
                return False

            elif s1_list[x] != s2_list[x] and swapped == False:
                s1_list[x] = s2_list[x]
                swapped = True

        return True

    return False


print(one_way("xey", "bey"))

# t1 = a,b
# t2 = a,b,c
# bbbbb bbbbc
# joined = a,b,c
# if diff between is same then its one way
# s.add(2 ) =>
# REPLACE
# WE KNOW S1.LEN == S2.len
# bool swap = false
# iterate through from 0 to len(s1)
# check every s1[x] == s2[x]
# if it's not true and swapped == True:
# return False
# its true and swapped == False -> then just do list[x] == list2[x]

# ADD or REPLACE
# BC AND DBC# -> BCD
# -> aebc aebc
# IF ITS ADD -> # 3