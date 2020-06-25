from models import *

def reconstruct(inOrder, start, end):

    if start > end or oob(inOrder, start) or oob(inOrder, end):
        return None

    mid = int(start + (end - start)/2)
    root = BinaryNode(inOrder[int(mid)])

    root.left = reconstruct(inOrder, start, mid-1)
    root.right = reconstruct(inOrder, mid+1, end)

    return root


def oob(arr, index):
    return index < 0 or index >= len(arr)

arr = [1,2,3,4,5,6,7]
test = reconstruct(arr, 0, len(arr)-1)

inOrder(test)