class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [] # holds [char, freq]
        
        for c in s:
            
            # if top is the same, don't add a new item, just increment freq
            if len(stk) > 0 and stk[-1][0] == c:
                stk[-1][1] += 1 
                
            # otherwise add a new item with freq of 1 
            else:
                stk.append([c, 1])
                
            # reached k elements, pop it from the stk string 
            if stk[-1][1] == k:
                stk.pop()
            
        res = ""
        for item in stk:
            res += item[0] * item[1]
            
        return res
            
                
        
        