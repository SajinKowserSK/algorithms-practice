def dutch_flag_sort(arr):
  print("\n")
  start_b = 0
  end_b = len(arr) - 1
  curr = 0

  while curr <= end_b:

    curr_elem = arr[curr]
    start_elem = arr[start_b]
    end_elem = arr[end_b]

    if curr_elem < 1:
        tmp = start_elem
        arr[start_b] = curr_elem
        arr[curr] = tmp

        start_b += 1
        curr += 1

    elif curr_elem > 1:

        tmp = end_elem
        arr[end_b] = curr_elem
        arr[curr] = tmp

        end_b -= 1

    else:
        curr += 1

  return arr



