# O(NK), O(1)
def max_sub_array_of_size_k(k, arr):
    max_sum = float('-inf')
    for x in range(0, len(arr)-k):
        curr_sum = 0
        for y in range(x, x+k):
            curr_sum += arr[y]
        max_sum = max(max_sum, curr_sum)
    return max_sum



def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  return -1
