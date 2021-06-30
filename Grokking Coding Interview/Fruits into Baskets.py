from collections import defaultdict

def fruits_into_baskets(fruits):
  fruit_types = defaultdict(lambda: 0)
  start_ptr = 0
  max_fruits = -float('inf') # flag

  for end_ptr in range(len(fruits)):
    right_char = fruits[end_ptr]
    fruit_types[right_char] += 1

    while len(fruit_types) > 2:
      left_char = fruits[start_ptr]
      fruit_types[left_char] -= 1

      if fruit_types[left_char] == 0:
        del fruit_types[left_char]

      start_ptr += 1

    max_fruits = max(max_fruits, end_ptr - start_ptr + 1)

  return max_fruits



