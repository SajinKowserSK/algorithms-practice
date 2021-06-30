def length_of_longest_substring(str, k):
  replacements = 0
  char_dict = {}
  single_char = str[0]
  start_ptr = 0

  longest = 0

  for end_ptr in range(len(str)):
    curr_char = str[end_ptr]
    char_dict[curr_char] = end_ptr # update last known position

    if curr_char != single_char:
      replacements += 1
      while replacements > k:
        left_char = str[start_ptr]
        start_ptr = char_dict[left_char] + 1 # shrink from left
        single_char = str[start_ptr]

        replacements = end_ptr - char_dict[single_char] # distance from closest position

    longest = max(longest, end_ptr - start_ptr + 1)

  return longest
