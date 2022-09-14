class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits)-1

        
        while x >= 0 and digits[x] == 9:
            x -= 1 

            
        if x == -1:
            return [1] + [0 for x in digits]
        
        else:
            digits[x] += 1 
            for x in range(x+1, len(digits)):
                digits[x] = 0
            
        return digits 
        