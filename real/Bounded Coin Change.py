def amazonFail(arr, target):
    dp = {}  # (i, s) index sum tuple

    def process(i, s):
        if (i, s) in dp:
            return dp[(i, s)]

        if s == 0:
            return 1

        if i == len(arr) or s < 0:
            return 0

        dp[(i, s)] = max(process(i + 1, s),  # dont take current coin
                         process(i + 1, s - arr[i]))  # take current coin

        return dp[(i, s)]

    return process(0, target)


print(amazonFail([-1, 7, 3, 4], 11))
print(amazonFail([-1, 7, 3, 4], 12))
print(amazonFail([-1, 7, 3, 4], 10))


