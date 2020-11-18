def slow_key(arr):
    longest = [arr[0][0], arr[0][1]]

    for x in range(1, len(arr)):

        curr = arr[x]
        prev = arr[x-1]

        diff = curr[1] - prev[1]

        if diff > longest[1]:
            longest[1] = diff
            longest[0] = curr[0]

    return chr(97 + longest[0])


print(slow_key([(0,2), (1,5), (0, 9), (2,15)]))