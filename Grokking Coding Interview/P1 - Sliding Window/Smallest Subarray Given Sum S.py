def smallest_subarray_with_given_sum(s, arr):
    # APPROACH 1 – O(n^2)
    # ret_val = float("inf")
    # found = False

    # for x in range(0, len(arr)):
    #   curr_len = 1
    #   curr_sum = arr[x]

    #   if curr_sum >= s:
    #     return curr_len

    #   for y in range(x+1, len(arr)):
    #     curr_sum += arr[y]
    #     curr_len += 1

    #     if curr_sum >= s:
    #       found = True
    #       ret_val = min(ret_val, curr_len)
    #       break

    # if found:
    #   return ret_val

    # return 0

    # APPROACH 2 – O(N)
    x = 0
    curr_sum = 0
    min_len = float("inf")

    while x < len(arr) and curr_sum < s:
        curr_sum += arr[x]
        x += 1

        # end is reached, did not sum to S
    if curr_sum < s:
        return 0

    min_len = x
    curr_len = x
    start = 0

    while x < len(arr):
        curr_sum += arr[x]
        curr_len += 1

        while curr_sum >= s:
            min_len = min(curr_len, min_len)
            curr_sum -= arr[start]
            curr_len -= 1
            start += 1

        x += 1

    return min_len














