import heapq
def fillTruck(num, boxes, unitSize, unitsPerBox, truckSize):
    packed_products = []
    for x in range(0, len(boxes)):
        curr_box = boxes[x]
        curr_product = unitsPerBox[x]

        entry = str(curr_product) * curr_box
        entry = list(entry)
        entry = [int(char) for char in entry]
        packed_products += entry

    packed_products = [num * -1 for num in packed_products]
    heapq.heapify(packed_products)

    size = 0
    i = 0

    while packed_products and i < truckSize:
        popped = heapq.heappop(packed_products)
        popped = abs(popped)
        size += popped

        i += 1

    return size

    # test case 1
boxes = [1,2,3]
num = len(boxes)
unitsPerBox = [3,2,1]
unitSize = len(unitsPerBox)
truckSize = 3

print(fillTruck(num, boxes, unitSize, unitsPerBox, truckSize))