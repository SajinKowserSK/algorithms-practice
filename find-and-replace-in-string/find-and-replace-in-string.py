class elem:
    def __init__(self, i, s, t):
        self.i = i 
        self.s = s
        self.t = t 

class Solution:

        
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        hmap = {}
        
        lst = [] 
        n = len(indices)
        
        zipped = sorted(
            [
                (indices[i], sources[i], targets[i])
                for i in range(n)
            ])
        
        pos = 0 
        res = ""
        
        for x in range(n):
            
            id_, src, tar = zipped[x]
            
            if pos > len(s) - 1:
                return res 
            
            # get string up until first replacement index
            res += s[pos:id_]
            
            # check if replacement index + len(src) in string == src
            
            if s[id_:id_+len(src)] == src:
                # update the pos to be after id_ + len(src)
                pos = id_ + len(src)
                res += tar
                
            else:
                pos = id_
                
        return res + s[pos:]
                
            
                
        
        
    
        
        
        
#         for x in range(0, len(sources)):
#             src = sources[x]
#             i = s.find(src, pos)
            
#             print(s, src, i, pos, "\n")
#             if i == indices[x]:
#                 hmap[src] = targets[x]
#                 pos += len(src)
                
#         # print(hmap)
#         for key in hmap:
            
#             s = s.replace(key, hmap[key])
            
        return s
            
            
        