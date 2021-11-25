"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
        

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        hmap = {} 
        for elem in employees:
            hmap[elem.id] = elem
            
        curr = hmap[id]
        final = curr.importance 
        for sub in curr.subordinates:
            final += self.getImportance(employees, sub)
            
        return final 
        
        
                
#         return final   
                
    
#     def helper(self, elem, total, hmap):

#         if len(elem.subordinates) == 0:
#             return elem.importance
        
#         else:
#             for sub in elem.subordinates:
#                 total += self.helper(hmap[sub], total, hmap)
                
#                 print("------------>", total)
                
#             return total + elem.importance
        
        
                
            
        