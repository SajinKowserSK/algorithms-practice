def merge(intervals_a, intervals_b):
    start, end = 0, 1
    result = []
    a_ptr = 0
    b_ptr = 0

    while a_ptr < len(intervals_a) and b_ptr < len(intervals_b):
        a = intervals_a[a_ptr]
        b = intervals_b[b_ptr]

        print(a, b, checkOverlap(a, b))

        if checkOverlap(a, b):
            curr = []
            curr.append(max(a[start], b[start]))
            curr.append(min(a[end], b[end]))

            result.append(curr)

        if a[end] < b[end]:
            a_ptr += 1

        else:
            b_ptr += 1

    return result


def checkOverlap(a, b):
    start, end = 0, 1
    lst = [a, b]
    lst.sort()

    a = lst[0]
    b = lst[1]

    if a[start] <= b[start] and a[end] >= b[start]:
        return True

    return False


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
