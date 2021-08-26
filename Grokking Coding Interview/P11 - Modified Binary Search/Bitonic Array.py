# def find_max_in_bitonic_array(arr):
#     start, end = 0, len(arr) - 1
#
#     while start <= end:
#         mid = start + (end - start) / 2
#         mid = int(mid)
#
#         if mid > 0 and mid < len(arr) - 1:
#             if arr[mid + 1] < arr[mid] > arr[mid - 1]:
#                 return arr[mid]
#
#             if arr[mid + 1] > arr[mid]:
#                 start = mid + 1
#
#             else:
#                 end = mid - 1
#
#         if mid == 0 and arr[mid] > arr[mid + 1]:
#             return arr[mid]
#
#         if mid == len(arr) - 1 and arr[mid] > arr[mid - 1]:
#             return arr[mid]
#
#     return -1

def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr)-1

    while start < end:
        mid = start + (end-start)/2
        mid = int(mid)

        if arr[mid+1] > arr[mid]:
            # we are still in the lesser half so make start = mid + 1
            start = mid + 1

        else:
            # arr mid is greater so its left could also be greater
            end = mid

    # both start and end will point to the max now because the condition to break is they equal each other
    return arr[start]



def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
