def find_range(arr, key):
    result = [- 1, -1]

    if binSearch(arr, key) == True:
        result[0] = largestSmall(arr, key)
        result[1] = smallestLarge(arr, key)

    return result


def binSearch(arr, key):
    if key > arr[-1]:
        return False

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key:
            return True

        elif arr[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return False


# assumes that we already have one occurence of the key
def largestSmall(arr, key):
    # print(find_range([4, 6, 6, 6, 9], 6))
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key or arr[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return end + 1  # returns largest smaller - 1 indice


def smallestLarge(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) / 2
        mid = int(mid)

        if arr[mid] == key or arr[mid] < key:
            start = mid + 1

        else:
            end = mid - 1

    return start - 1


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
