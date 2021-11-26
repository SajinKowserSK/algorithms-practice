class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        hmap = {}
        final, currlen, start = 0, 0, 0
        
        for end in range(len(s)):
            char = s[end]
            
            
            if char not in hmap:
                hmap[char] = end 
                currlen += 1 
                
                
                final = max(final, currlen)
                
            else:
                print("CURR CHAR IS", char, "POSITION", end)
                
                i = hmap[char]
                oldstart = start
                start = i + 1 
                
                for x in range(oldstart, start):
                    del hmap[s[x]]
                    
                    
                currlen = end - start + 1 
                hmap[char] = end
                
                print("AFTER SHIFT START IS", start, "END IS", end)
              
                
        return final 
                
                