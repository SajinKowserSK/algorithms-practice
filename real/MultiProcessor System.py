# go through ability and put it into max heap
# counter = 0

import heapq
from math import floor
def process(num, ability, process):
    heap = []
    heapq.heapify(heap)
    for ab in ability:
        heapq.heappush(heap, ab*-1)

    counter = 0
    while process > 0:
      popped = heapq.heappop(heap)
      process -= abs(popped)
      heapq.heappush(heap, floor(abs(popped)/2))
      counter += 1
    return counter

test = [3,1,7,2,4]
print(process(len(test), test, 15))



