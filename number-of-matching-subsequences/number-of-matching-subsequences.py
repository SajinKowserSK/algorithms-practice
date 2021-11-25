class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        out = 0 
        for word in words:
            wlist = list(word)
            ok = True 
            
            pos = -1
            for char in wlist:
            
                i = s.find(char, pos+1)
                if i < pos or i == -1:
                    ok = False 
                    break
                    
                pos = i 
            
            if ok == True:
                out += 1 
                
        return out 
                    
                
                    
                
                    
                
                
            
        