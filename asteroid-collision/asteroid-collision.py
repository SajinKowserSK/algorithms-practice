class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = [] 
        for ast in asteroids:
            while stk and stk[-1] > 0 and ast < 0:
                collision = stk[-1] + ast
                if collision > 0: # peak is greater
                    ast = 0 
                    
                elif collision == 0:
                    ast = 0 
                    stk.pop(-1) 
                    
                else: # incoming is greater
                    stk.pop(-1)
                    
            if ast:
                stk.append(ast)
                    
                    
            
        return stk
                        
                        
            
        
        