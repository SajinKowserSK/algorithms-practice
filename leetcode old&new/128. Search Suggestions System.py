class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        globalL = []
        lstChars = list(searchWord)

        products.sort()

        for x in range(0, len(lstChars)):
            curr_sub = "".join(lstChars[0:x + 1])
            curr_lst = []

            for string in products:

                if len(curr_lst) == 3:
                    break

                if curr_sub in string[0:x + 1]:
                    curr_lst.append(string)

            globalL.append(curr_lst)

        return globalL


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []

        products.sort()

        left = 0
        right = len(products) - 1

        for i in range(len(searchWord)):

            while left <= right and (len(products[left]) <= i or products[left][i] != searchWord[i]):
                left += 1

            while left <= right and (len(products[right]) <= i or products[right][i] != searchWord[i]):
                right -= 1

            if left + 3 <= right:
                output.append(products[left:left + 3])
            else:
                output.append(products[left:right + 1])

        return output
