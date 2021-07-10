def search_triplets(arr):
  triplets = []
  arr.sort()

  for x in range(0, len(arr)):
      curr_num = arr[x]
      sum_zero = curr_num

      start = x + 1
      end = len(arr) - 1

      while start < end:

          left = arr[start]
          right = arr[end]


          total_sum = left + right + sum_zero

          print(left, right, total_sum,  curr_num)

          if total_sum == 0:
              triplets.append([arr[x], left, right])
              break

          elif total_sum > 0:
              end -= 1

          else:
              start += 1

  return triplets



print(search_triplets([-5, 2, -1, -2, 3]))


