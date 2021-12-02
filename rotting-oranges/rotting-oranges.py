from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # create adjacency list where {pos: tuple(max len of 4 neighbors)}
        # iterate through matrix and add all the rotten ones to the dq
        # safeOnes = # of safe ones as well 
        # while dq: -> for nbr in dq.popleft() -> mark as rotten, subtract from safe 
        # check if safe is 0 -> return minutes 
        
        safe = 0 
        rotten = []
        dq = deque() 
        
        
        for row in range(len(grid)):
            
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    safe += 1 
                    
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        minutes = 0 
        dq = deque(rotten)
        if safe == 0:
            return minutes 
        
        safe = [safe]
        while dq:

            levelSize = len(dq)
            for _ in range(levelSize):
                currPopped = dq.popleft() #coordinate of rotten orange 
        
                retStatus = [0] 
                self.checkNeighbors(grid, currPopped[0], currPopped[1], safe, dq, retStatus)
                # print(grid, "\n")
                              
                if retStatus[0] == 1:
                    return minutes + 1 
                
            minutes += 1 
            
        return -1
                
                
                    
    def checkNeighbors(self, grid, x, y, safe, dq, retStatus):
        # x + 1 < len(grid)
        # x - 1 >= 0 
        # y + 1 < len(grid[x])
        # y - 1 >= 0
        
        nbrs = [(x + 1, y),
               (x - 1, y),
               (x, y + 1),
               (x, y - 1)]
        
        for nbr in nbrs:
            if nbr[0] < len(grid) and nbr[0] >= 0 and nbr[1] < len(grid[nbr[0]]) and nbr[1] >= 0:
                row = nbr[0]
                col = nbr[1]
                
                if grid[row][col] == 1:
                    # fresh orange found 
 
                    safe[0] -= 1 
                    grid[row][col] = 2
                    dq.append((row, col))
                    if safe[0] == 0:
                        retStatus[0] = 1 
                        
                else:
                    continue 
          
                              
            
                
            
        
            
            
        
        