
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

print(count([1,5,5,1,5,1], 6))
print(count2([1,5,5,1,5,1], 6))

print(count([1, 1, 2, 45, 46, 46], 47))
print(count2([1, 1, 2, 45, 46, 46], 47))