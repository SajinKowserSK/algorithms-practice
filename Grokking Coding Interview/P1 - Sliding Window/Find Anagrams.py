from _collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        retL = []

        ch_dict = defaultdict(lambda: 0)
        start_ptr = 0
        matched = 0

        for ch in p:
            ch_dict[ch] += 1

        for end_ptr in range(len(s)):
            right_char = s[end_ptr]

            if right_char in ch_dict:
                ch_dict[right_char] -= 1

                if ch_dict[right_char] == 0:
                    matched += 1

            if matched == len(ch_dict):
                retL.append(start_ptr)

            if end_ptr >= len(p) - 1:
                left_char = s[start_ptr]
                start_ptr += 1

                if left_char in ch_dict:
                    if ch_dict[left_char] == 0:
                        matched -= 1

                    ch_dict[left_char] += 1

        return retL