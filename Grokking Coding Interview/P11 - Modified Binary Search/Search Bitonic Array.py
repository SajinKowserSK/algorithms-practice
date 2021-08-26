def search_bitonic_array(arr, key):
    indexOfMax = maxBitonic(arr)
    leftOfMax = bs(0, indexOfMax, arr, key)
    rightOfMax = bs(indexOfMax + 1, len(arr) - 1, arr, key)

    if leftOfMax >= 0:
        return leftOfMax

    if rightOfMax >= 0:
        return rightOfMax

    return -1


def bs(start, end, arr, key):
    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1


def maxBitonic(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid + 1] > arr[mid]:
            # we are in ascending half
            start = mid + 1

        else:
            # descending half
            # max can be mid or to the left
            end = mid

    return start


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
