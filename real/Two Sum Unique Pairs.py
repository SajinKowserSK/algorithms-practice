
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

    return len(results)


def count2(arr, target):
    arr.sort()
    count = 0
    start = 0
    end = len(arr)-1

    prev_start = None

    while start <= end:

        if prev_start != None and arr[start] == arr[prev_start]:
            start += 1
            continue

        sum = arr[start] + arr[end]

        if sum == target:

            count += 1

            prev_start = arr[start]

            start += 1
            end -= 1

        elif sum < target:
            start += 1

        else: # sum > target
            end -= 1

    return count


def count3(arr, t):
    map1 = {}
    ans = set()
    for x in range(0, len(arr)):
        elem = arr[x]

        if t - elem in map1:
            ans.add((elem, arr[map1[t-elem]]))

        else:
            map1[elem] = x

    return len(ans)

print(count([1, 1, 2, 45, 46, 46], 47))
print(count2([1, 1, 2, 45, 46, 46], 47))
print(count3([1, 1, 2, 45, 46, 46], 47))