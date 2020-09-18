from models import BinaryNode

# TEST 1
# root = BinaryNode("A")
# root.left = BinaryNode("B")
# root.left.left = BinaryNode("D")
# root.right=BinaryNode("C")
# root.right.left = BinaryNode("E")
# root.right.right = BinaryNode("F")

# TEST 2
root = BinaryNode("A")
root.left = BinaryNode("B")
root.left.left = BinaryNode("C")
root.left.left.left = BinaryNode("E")
root.left.left.right = BinaryNode("D")

def print_bin_node(lst):
    for x in range(0, len(lst)):
        try:
            lst[x] = lst[x].data
        except:
            continue
    return lst

def print_paths(root, lst):
    if root is None:
        return []

    elif root.left is None and root.right is None:
        lst.append(root)
        print(print_bin_node(lst))
        lst.pop(-1)

    else:
        lst.append(root)
        print_paths(root.left, lst)
        print_paths(root.right, lst)
        lst.pop(-1)

print_paths(root, [])






class NodeLL:

    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next


e1 = NodeLL("Mon")
e2 = NodeLL("Tues")
LL = LinkedList()
LL.head = e1
e1.next = e2
# LL.show()





# find min in cyclically sorted array

def findMin(arr):
    if arr is None:
        return None

    start = 0
    end = len(arr)-1
    right_most = arr[len(arr)-1]


    while start <= end:
        mid = int(start + (end - start)/ 2)

        if arr[mid] <= right_most and mid == 0 or arr[mid-1] > arr[mid]:
            return mid

        elif arr[mid] > right_most:
            start = mid + 1

        else:
            end = mid - 1

    return None


# print(findMin([3,4,5,6,7,1,2]))


# binary search w duplicates
# return index of where to put target in log time

def search(arr, target):
    if arr is None:
        return None

    start = 0
    end = len(arr)-1
    closest = None
    closest_index = None

    while start <= end:
        mid = int(start + (end-start)/2)
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            diff = arr[mid] - target
            if closest is None or diff <= closest:
                closest = diff
                closest_index = mid

            end = mid - 1

        else:
            return mid

    if closest_index is None:
        closest_index = len(arr)-1

    return closest_index


# print(search([5,5,6], 4))

# shortest unsorted
# identify dip
# identify bump
# identify minimum in that subarray arr[dip:bump]
# go left from the minimum
# return minimum:bump+1
def find(arr):
    if arr is None or len(arr) == 0:
        return None

    dip = None
    for x in range (1, len(arr)):
        if arr[x] < arr[x-1]:
            dip = x
            break

    if dip is None:
        return None

    for x in range(len(arr)-1, 0, -1):
        if arr[x-1] > arr[x]:
            bump = x
            break

    min = arr[dip]
    min_index = dip
    for x in range(dip, bump):
        if arr[x] < min:
            min = arr[x]
            min_index = x

    for x in range(min_index, -1, -1):
        if arr[min_index] > arr[x]:
            min_index = x+1
            break

    return (min_index, bump)


# print(find([1,3,5,2,6,4,7,8,9]))