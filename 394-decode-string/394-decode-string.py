class Solution:
    def decodeString(self, s: str) -> str:
        stk = [] 
        for c in s:
            if c != "]":
                stk.append(c)
                
            else:
                tmp = ""
                while stk[-1] != "[":
                    popped = stk.pop()
                    tmp = popped + tmp 
                    
                stk.pop() # gets rid of [
                
                freqTmp = ""
                while stk and stk[-1].isnumeric(): 
                    freqTmp = stk.pop() + freqTmp 

                tmp = tmp * int(freqTmp)
                stk.append(tmp) # put back into stk 
                
        return "".join(stk)
        