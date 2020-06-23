# def searchInsert(arr, target):
#     start = 0
#     end = len(arr)-1
#
#     while (start <= end):
#
#         mid = int(start+(end-start)/2)
#
#         if arr[mid] <= target:
#             if arr[mid] == target or mid == len(arr)-1:
#                 return mid
#
#             start = mid + 1
#
#         else:
#             if mid == 0 or arr[mid-1] == target:
#                 return mid
#
#             end = mid - 1
#
# sajin = [1,2,3,4,5,6]
# print(searchInsert(sajin, 2))
#


prac = [1,2]
prac.remove(prac[0])
print(prac)

