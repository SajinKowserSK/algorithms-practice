class Solution(object):
    
    def findContentChildren(self, g, s):
        # sort both lists
        # for x in children list 
        # for x in cookie size list 
        # if cookie size >= greed factor 
        # counter++ and list. remove[x] 
        # break
        # return counter
        
        g.sort()
        s.sort() 
        
        counter = 0
        for x in range (0, len(g)):
            for y in range (0, len(s)):
                if s[y] >= g[x]:
                    counter = counter + 1
                    s.remove(s[y])
                    break
        
        return counter
        
        