
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        new_para = ""

        for x in range(0, len(paragraph) - 1):
            char = paragraph[x]
            next_char = paragraph[x + 1]
            if (char == "," or char == "." or char == "?" or char == "!") and next_char != " ":
                new_para += char
                new_para += " "

            else:
                new_para += char

        new_para += paragraph[-1]

        map1 = {}

        banned_words = set()

        for elem in banned:
            banned_words.add(elem)

        lst_str = new_para.split()

        print(lst_str)

        for word in lst_str:

            new_word = ""
            for char in word:
                if char.isalpha():
                    new_word += char

            new_word = new_word.lower()
            if new_word not in banned_words:
                map1[new_word] = map1.get(new_word, 0) + 1

        max_count = 0

        map2 = {}

        for key in map1:
            max_count = max(map1[key], max_count)
            map2[map1[key]] = key

        ans = map2[max_count]
        return ans.lower()





