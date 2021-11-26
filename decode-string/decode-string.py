class Solution:
    def decodeString(self, s: str) -> str:
        
        lstk = [] # for ints
        rstk = [] # for chars and brackets
        
        lst = list(s)
        
        while lst:
            popped = lst.pop(0)
            
            if popped.isdigit():
                digit = popped
                while lst[0].isdigit():
                    popped = lst.pop(0)
                    digit += popped
                
                lstk.insert(0, digit)
                
            else:
                if popped == "]":
           
                    currStr = ""
                    peek = rstk[0]
                    
                    while peek != "[":
                        currStr = peek + currStr
                        rstk.pop(0)
                        peek = rstk[0]
                        
                    if peek == "[":
                        rstk.pop(0)
                        currNum = lstk.pop(0)
                        currStr = int(currNum) * currStr 
                        rstk.insert(0, currStr)
                        
                else:
                    rstk.insert(0, popped)
           
        final = ""
        while rstk:
            popped = rstk.pop(0)
            final = popped + final 
            
        return final
                        
                
            
        
        
        
                
            
        