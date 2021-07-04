class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = defaultdict(lambda: 0)
        start_ptr = 0
        matched = 0

        for ch in s1:
            char_dict[ch] += 1

        for end_ptr in range(len(s2)):
            right_char = s2[end_ptr]

            if right_char in char_dict:
                char_dict[right_char] -= 1

                if char_dict[right_char] == 0:
                    matched += 1

            print(char_dict, matched)
            if matched == len(char_dict):
                return True

            while (end_ptr - start_ptr + 1) >= len(s1):
                left_char = s2[start_ptr]
                if left_char in char_dict:
                    if char_dict[left_char] == 0:
                        matched -= 1
                    char_dict[left_char] += 1

                start_ptr += 1

        return False