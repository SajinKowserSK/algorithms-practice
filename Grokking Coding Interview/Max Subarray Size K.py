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
  start = 0
  end = k-1
  max_sum = float("-inf")

  curr_sum = 0

  for x in range(start, k):
      curr_sum += arr[x]

  while end < len(arr):
      max_sum = max(max_sum, curr_sum)
      curr_sum += arr[end+1]
      curr_sum -= arr[start]

      start += 1
      end += 1

  return max_sum
