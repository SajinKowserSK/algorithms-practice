class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []

        for char in ops:
            print(scores)
            if char.isdigit() or (len(char) > 1 and char[0] == "-"):
                scores.append(int(char))

            elif char == "C":
                scores.pop(-1)

            elif char == "D":
                prev = scores[-1]
                scores.append(prev * 2)

            elif char == "+":
                prev = scores[-1]
                sec_prev = scores[-2]

                scores.append(prev + sec_prev)

        return sum(scores)




