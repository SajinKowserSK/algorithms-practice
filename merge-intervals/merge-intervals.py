class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        lst = [] 
        intervals.sort(key=lambda x:x[0]) # sort by meeting start times 
        lst.append(intervals[0])
        
        x = 1 
        
        while x < len(intervals):
            start, end = intervals[x]
            if start <= lst[-1][-1]:
                lst[-1][-1] = max(lst[-1][-1], end)
                
            else:
                lst.append(intervals[x])
            x += 1 
        
        return lst
            
            
        