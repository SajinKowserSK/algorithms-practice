def countPairs(a, n):
    # Storing occurrences of each element
    mp = dict.fromkeys(a, 0)
    for i in range(n):
        mp[a[i]] += 1

    # Sort the array in deceasing order
    a.sort(reverse=True)

    # Start taking largest element
    # each time
    count = 0
    for i in range(n):

        # If element has already been paired
        if (mp[a[i]] < 1):
            continue

        # Find the number which is greater
        # than a[i] and power of two
        cur = 1
        while (cur <= a[i]):
            cur = cur << 1

        # If there is a number which adds
        # up with a[i] to form a power of two
        if (cur - a[i] in mp.keys()):

            # Edge case when a[i] and crr - a[i]
            # is same and we have only one occurrence
            # of a[i] then it cannot be paired
            if (cur - a[i] == a[i] and mp[a[i]] == 1):
                continue

            count += 1

            # Remove already paired elements
            mp[cur - a[i]] -= 1
            mp[a[i]] -= 1

    # Return the count
    return count


# Driver code
if __name__ == "__main__":
    a = [3, 3, 5, 11,14,5,13]
    n = len(a)
    print(countPairs(a, n))