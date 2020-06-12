import pdb


def pair(x, y):
    return ("("+str(x)+", "+str(y)+")")

def subArr(arr):

    for x in range (0, len(arr)):
        start = x
        sum = 0

        for y in range (x, len(arr)):
            sum = sum + arr[y]

            if sum == 8:
                return pair(x, y)

            elif sum > 8:
                break

    return None
print(subArr([1,2,3,5,2]))