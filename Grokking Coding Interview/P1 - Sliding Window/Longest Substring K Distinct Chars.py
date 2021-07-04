from collections import defaultdict


def longest_substring_with_k_distinct(str1, k):
    char_dict = defaultdict(lambda: 0)
    start_ptr = 0
    longest = float('-inf')
    # expanding window right
    for end_ptr in range(len(str1)):
        end_char = str1[end_ptr]
        char_dict[end_char] += 1

        # limit reached, have to minimize window from left
        while len(char_dict) > k:
            start_char = str1[start_ptr]
            char_dict[start_char] -= 1

            if char_dict[start_char] == 0:
                del char_dict[start_char]

            start_ptr += 1

        longest = max(longest, end_ptr - start_ptr + 1)

    return longest
