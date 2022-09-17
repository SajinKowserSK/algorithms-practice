class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = [] # each item [char, freq]
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1 
                
            else:
                stk.append([c, 1])
                
            if stk[-1][1] == 2:
                stk.pop()
                
        res = ""
        for c in stk:
            res += c[0]
            
        return res 
        