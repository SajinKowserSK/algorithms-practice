class Solution:
    def removeStars(self, s: str) -> str:
        stk = [] 
        
        for c in s:
            if c == "*":
                stk.pop() 
                
            else:
                stk.append(c)
                
        res = ""
        for c in stk:
            res += c
            
        return res 
        