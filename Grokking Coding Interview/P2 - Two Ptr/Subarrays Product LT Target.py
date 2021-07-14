def find_subarrays(arr, target):
  result = []
  product = 1

  for x in range(0, len(arr)):
      curr_list = []

      for y in range(x, len(arr)):
          product *=  arr[y]


          if product < target:
              curr_list.append(arr[y])
              result.append(list(curr_list))



          else:
              product = 1
              break

  return result

print(find_subarrays([2,5,3,10], 30))
print(find_subarrays([8, 2, 6, 5], 50))
