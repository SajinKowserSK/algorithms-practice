class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        p = sorted(A, key=abs)
        
        for x in p:
            if count[x] == 0:
                continue 
                
            if (x*2) not in count or count[x*2] == 0:
                return False # already taken 
            
            else:
                count[x*2] -= 1 
                count[x] -= 1 

        return True