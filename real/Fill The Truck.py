# TC -> O(n * m) for first part, O(nmlognm) for heap part
# SC -> O(n)


import heapq
def fillTruck(num, boxes, unitSize, unitsPerBox, truckSize):

    # first create list where "box" occurs unitsPerBox times
    # ie boxes = [1,2,3] and unitsPerBox = [3,2,1] -> product 0 will be 1 box and 3 times so [1,1,1], insert at front
    packed_products = []
    for x in range(0, len(boxes)):
        curr_box = boxes[x]
        curr_product = unitsPerBox[x]

        entry = str(curr_product) * curr_box
        entry = list(entry)
        entry = [int(char) for char in entry]
        packed_products += entry


    # multiply them by -1 so we can get a max heap
    packed_products = [num * -1 for num in packed_products]
    heapq.heapify(packed_products)

    size = 0
    i = 0

    # pop it amount of times = truck size
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