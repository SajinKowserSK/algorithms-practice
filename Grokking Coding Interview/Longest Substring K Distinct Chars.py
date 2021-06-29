from collections import defaultdict
# optimized soln
def longest_substring_with_k_distinct(str1, k):
  longest = float("-inf")
  char_dict = defaultdict(lambda: 0)
  dict_size = 0
  startptr = 0
  curr_len = 0

  for endptr in range(0, len(str1)):
    char = str1[endptr]
    # can optimize approach next time by putting indice in the value instead of how
    # often the key occurs
    if char not in char_dict:
      char_dict[char] += 1
      dict_size += 1
    curr_len += 1
    if dict_size > k:
      char_dict.pop(char)
      dict_size -= 1
      endptr -= 1
      curr_len -= 1
      break

  longest = max(longest, curr_len)
  endptr += 1
  while endptr < len(str1):
    char = str1[endptr]
    if char in char_dict:
      curr_len += 1
    else:
      if dict_size == k:
        # shrink from left
        firstchar = str1[startptr]
        char_dict.pop(firstchar)
        dict_size -= 1

        while str1[startptr] == firstchar:
          startptr += 1
          curr_len -= 1

      # expand to right
      char_dict[char] += 1
      dict_size += 1
      curr_len += 1

    longest = max(longest, curr_len)
    endptr += 1

  return longest


# brute force solution

from collections import defaultdict

# O(n^2) TC
# O(n) SC

def longest_substring_with_k_distinct(str1, k):
  max_len = float("-inf")
  for x in range(0, len(str1)):
    chars = defaultdict(lambda: 0)
    curr_len = 0
    for y in range(x, len(str1)):
      # can optimize by adding elif case to update unique chars in constant time
      # instead of len() linear time
      if len(chars) < k or str1[y] in chars:
        chars[str1[y]] += 1
        curr_len += 1
      else:
        break
    max_len = max(max_len, curr_len)
  return max_len