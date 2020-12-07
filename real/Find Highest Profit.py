import heapq
def highestProfit(numSuppliers, inventory, order):
    heap = []
    heapq.heapify(heap)

    for item in inventory:
        item_val = -1 * item
        heapq.heappush(heap, item_val)


    profit = 0
    while order > 0 and heap:
        popped = heapq.heappop(heap)
        profit += abs(popped)
        push_back = popped + 1
        heapq.heappush(heap, push_back)
        order -= 1

    print(profit)
    return profit


highestProfit(2, [3,5], 6)
