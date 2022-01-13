from collections import deque 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {}
        inbounds = {} 
        sources = deque() 
        
        finalOrder = []
        
        for x in range(numCourses):
            adjList[x] = []
            inbounds[x] = 0 
            
        for course, prereq in prerequisites:
            inbounds[course] += 1 
            adjList[prereq].append(course)
            
        for key in inbounds:
            if inbounds[key] == 0:
                sources.append(key)

        while sources:
            popped = sources.popleft()
            nbrs = adjList[popped]
            
            for nbr in nbrs:
                inbounds[nbr] -= 1 
                if inbounds[nbr] == 0:
                    sources.append(nbr)
                    
            finalOrder.append(popped)
            
        if len(finalOrder) != numCourses:
            return []
            
        
        return finalOrder
            
        