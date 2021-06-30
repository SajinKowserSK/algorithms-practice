# O(26) -> O(1) SC, O(N) TC

def non_repeat_substring(str):
  char_dict = {}
  longest = 0
  start_ptr = 0

  for end_ptr in range(len(str)):
    right_char = str[end_ptr]
    if right_char in char_dict:
      curr_len = end_ptr - start_ptr
      longest = max(longest, curr_len)
      start_ptr = char_dict[right_char] + 1 # set left ptr to right of last occurence

    char_dict[right_char] = end_ptr
    longest = max(longest, end_ptr - start_ptr + 1)

  return longest

