class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0 
        
        rStr = list(s)
        lStr = []
        rCounter, lCounter, counter = 0, 0, 0
        lMap, rMap = {}, {}
        
        for char in rStr:
            if char not in rMap:
                rMap[char] = 0
                rCounter += 1 
                
            rMap[char] += 1 
            
        print(rMap, lMap, rCounter, lCounter)
        
        while len(rStr) > 1:
            rPop = rStr.pop(0)
            rMap[rPop] -= 1
            
            if rMap[rPop] == 0:
                del rMap[rPop] 
                rCounter -= 1
                
                
            if rPop not in lMap:
                lMap[rPop] = 0
                lCounter += 1 
                
            lMap[rPop] += 1 
            
            if rCounter == lCounter:
                counter += 1 
                
        return counter 