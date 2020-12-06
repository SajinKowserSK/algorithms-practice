# BRUTE FORCE: O(N * M Squared) TC and O(N) Space
# go through list and make substring of start to that character
# then check that string against every character in product
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


# OPTIMIZED: O(m log m) for product sort, O(n * log n) for n times binary search + O( m log n)
# TC -> O(nlogn) + O(mlogm) SC -> O(n) for output or O(1)
# SC -> O(1) if output array doesn't count
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []

        products.sort()

        left = 0
        right = len(products) - 1

        # for every character indice, check if products at left nad right have the same at the same indice
        # because they're lexi-g sorted, everything in between will also have that
        for i in range(len(searchWord)):

            while left <= right and (len(products[left]) <= i or products[left][i] != searchWord[i]):
                left += 1

            while left <= right and (len(products[right]) <= i or products[right][i] != searchWord[i]):
                right -= 1

            # include left + 3 if thats before right otherwise right
            if left + 3 <= right:
                output.append(products[left:left + 3])
            else:
                output.append(products[left:right + 1])

        return output
