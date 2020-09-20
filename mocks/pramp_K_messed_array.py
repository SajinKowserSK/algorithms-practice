## HELPERS AND STARTING CLASSES

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3 -> 4 -> 3 -> 2 -> 5 -> 5 -> 7

arr = [3,4,3,2,5,5,7]
def create_LL(arr):
    for x in range(0, len(arr)):
        arr[x] = Node(arr[x])

    for x in range(0, len(arr)-1):
        arr[x].next = arr[x+1]

    return arr[0]


case = create_LL(arr)

## QUESTION
def condense(case):
    curr = case
    vals = []

    while curr is not None:
        vals.append(curr.data)
        unique = find_unique(curr.next, vals)
        curr.next = unique

        if unique is not None:
            vals.append(unique.data)

        curr = curr.next

    return case


def find_unique(node, vals):
    print(node.data)
    while node is not None:
        if node.data not in vals:
            return node

    return None


def print_ll(node):
    while node is not None:
        print(node.data)
        node = node.next

ans = condense(case)




