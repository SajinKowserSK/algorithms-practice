from heapq import *

def solution(n):
    minHeap = []
    retStr = ""
    n = str(n)
    lst = []
    for char in n:
        lst.append(char)

    for x in range(len(lst)):
        lst[x] = int(lst[x])
        heappush(minHeap, -lst[x])


    for x in range(0, 3):
        s = -heappop(minHeap)
        retStr += str(s)

    return int(retStr)
#
# print(solution(30919))
# print(solution(328))
# print(solution(240))


def solution(S):
    words = S.split("-")
    if len(words[0]) < 3 or len(words[1]) < 3:
        return False

    suffix1 = []
    suffix2 = []
    for y in range(len(words[0])-1, len(words[0])-4, -1):
        suffix1.append(words[0][y])

    for y in range(len(words[1])-1, len(words[1])-4, -1):
        suffix2.append(words[1][y])

    for y in range(len(suffix1)):
        if suffix1[y] != suffix2[y]:
            return False

    return True


print(solution("news-views"))
print(solution("at-cat"))
print(solution("football-allal"))
print(solution("-pet"))
#
# def find_Kth_smallest_number(nums, k):
#   # TODO: Write your code here
#   minHeap = []
#
#   for x in range(k):
#       heappush(minHeap, nums[x])
#
#   for x in range(k+1, len(nums)):
#       if minHeap[-1] > nums[x]:
#           minHeap.pop(-1)
#           heappush(minHeap, nums[x])
#
#
#   return list(minHeap)[-1]
#
#
# def main():
#
#   print("Kth smallest number is: " +
#         str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))
#
#   # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
#   print("Kth smallest number is: " +
#         str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))
#
#   print("Kth smallest number is: " +
#         str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))
#
#
# main()
