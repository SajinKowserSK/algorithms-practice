from heapq import *


def sort_character_by_frequency(str):
    maxHeap = []
    hmap = {}
    for char in str:
        if char in hmap:
            hmap[char] += 1

        else:
            hmap[char] = 1

    for char, freq in hmap.items():
        heappush(maxHeap, (-freq, char))

    res = []
    while maxHeap:
        popped_tuple = heappop(maxHeap)
        for x in range(-popped_tuple[0]):
            res.append(popped_tuple[1])

    return "".join(res)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
