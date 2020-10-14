def climbStairs(n):
    if n == 0 or n == 1 or n == 2:
        return n

    return memoize(n)

def memoize(n):
    cache = {0: 0, 1: 1, 2: 2}
    for x in range(3, n + 1):
        cache[x] = cache[x - 1] + cache[x - 2]

    return cache[n]


# test cases

# print(climbStairs(4)) # 5
# print(climbStairs(5)) # 8