def search_min_diff_element(arr, key):
    left = leftLargest(arr, key)
    right = rightSmallest(arr, key)

    diffLeft = abs(arr[left] - key)
    diffRight = abs(arr[right] - key)

    if diffLeft < diffRight:
        return arr[left]

    else:
        return arr[right]


def leftLargest(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            start = mid + 1

        else:
            end = mid - 1

    return min(len(arr) - 1, max(0, end))


def rightSmallest(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            start = mid + 1

        else:
            end = mid - 1

    return max(0, min(start, len(arr) - 1))


