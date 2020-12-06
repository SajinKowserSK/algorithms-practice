# O(N) time and O(N) space can also do (Nlogn) time and O(1) space w two pointer
def givenSum(arr, target):
    map = {}
    ans = set()

    # construct ans set
    for x in range(0, len(arr)):
        val = arr[x]
        diff = target - val

        if diff in map:
            partner = map[diff]
            partner = arr[partner]

            entry = (max(partner, val), min(partner, val))
            ans.add(entry)

        else:
            map[val] = x

    largest = float("-inf")
    pair = None

    for max_val, min_val in ans:
        if max_val > largest:
            pair = (max_val, min_val)
            largest = max_val


    return list(pair)


print(givenSum([20, 50, 40, 25, 30, 10], 60))


