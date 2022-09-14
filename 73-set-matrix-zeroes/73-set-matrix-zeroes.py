from collections import deque 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        dq = deque() 
        
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == 0:
                    dq.append((row, col))
        
        for pt in dq:
            self.clear(matrix, pt)
                    
    
    def clear(self, matrix, pt):
        x, y = pt[0], pt[1]
        r = y + 1 
        l = y -1 
        u = x - 1 
        d = x + 1 
        
        while r < len(matrix[0]):
            matrix[x][r] = 0 
            r += 1 
            
        while l >= 0: 
            matrix[x][l] = 0
            l -= 1 
            
        while u >= 0:
            matrix[u][y] = 0
            u -= 1 
            
        while d < len(matrix):
            matrix[d][y] = 0
            d += 1 
            
        
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        