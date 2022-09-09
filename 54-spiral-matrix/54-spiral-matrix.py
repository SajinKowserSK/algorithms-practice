class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = [] 
        seen = set()
        
        self.goRight(ans, seen, matrix, (0,0))
        return ans 
        
    def checkOOB(self, p, matrix):
        if 0 <= p[0] < len(matrix):
            if 0 <= p[1] < len(matrix[0]):
                return False 
            
        return True 
        
    def getNextValidCell(self, p, matrix, direc):
        if direc == "right":
            return (p[0]+1, p[1]-1)
        
        if direc == "down":
            return (p[0]-1, p[1]-1)
        
        if direc == "left":
            return (p[0]-1, p[1]+1)
        
        if direc == "up":
            return (p[0]+1, p[1]+1)
        
    def goRight(self, ans, seen, matrix, p):
        if len(ans) == len(matrix[0])*len(matrix):
            return 
            
        r, c = p[0], p[1]
        
        while self.checkOOB((r, c), matrix) == False and (r, c) not in seen:
            ans.append(matrix[r][c])
            seen.add((r, c))
            c += 1 
            
            
        self.goDown(ans, seen, matrix, self.getNextValidCell((r,c), matrix, "right"))
            
        
    def goDown(self, ans, seen, matrix, p):
        if len(ans) == len(matrix[0])*len(matrix):
            return 
        r, c = p[0], p[1]
        while self.checkOOB((r, c), matrix) == False and (r, c) not in seen:
            ans.append(matrix[r][c])
            seen.add((r, c))
            r += 1 
            
        self.goLeft(ans, seen, matrix, self.getNextValidCell((r,c), matrix, "down"))
        
    def goUp(self, ans, seen, matrix, p):
        if len(ans) == len(matrix[0])*len(matrix):
            return 
        r, c = p[0], p[1]
        while self.checkOOB((r, c), matrix) == False and (r, c) not in seen:
            ans.append(matrix[r][c])
            seen.add((r, c))
            r -= 1 
            
        self.goRight(ans, seen, matrix, self.getNextValidCell((r,c), matrix, "up"))

        
    def goLeft(self, ans, seen, matrix, p):
        if len(ans) == len(matrix[0])*len(matrix):
            return 
        r, c = p[0], p[1]
        while self.checkOOB((r, c), matrix) == False and (r, c) not in seen:
            ans.append(matrix[r][c])
            seen.add((r, c))
            c -= 1 
            
        self.goUp(ans, seen, matrix, self.getNextValidCell((r,c), matrix, "left"))