
def count(arr, target):
    count = 0
    results = set()
    vals = set()

    for val in arr:
        diff = target - val

        if diff in vals:
            pair = (val, diff)
            results.add(pair)

        else:
            vals.add(val)

    print(results)
    return len(results)


print(count([1,5,5,1,5,1], 6))
