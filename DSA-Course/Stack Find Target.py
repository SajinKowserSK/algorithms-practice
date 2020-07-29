'''

                            O(n) soln with O(1) space apparently. Even though we allocated another stack, since we moved the objects back to the original, it's apparently
                            O(1). Very interesting, will have to check with someone.

'''

class stack:
    def __init__(self):
        self.arr = [] 
        
    
    def push(self, item):
        self.arr.insert(0, item)
        
    def pop(self):
        return self.arr.pop(0)
        

    def peek(self):
        return self.arr[0]
        
    def size(self):
        return len(self.arr)

def findTarget(num, stk):
    
    if stk is None or num is None:
        return None 
    
    stk2 = stack()
    
    while stk.size() != 0: 

        
        tmp = stk.pop()
        
        if tmp == num:
            return True 
            
        else:
            stk2.push(tmp)
        
        
    while stk2.size() != 0:
        stk.push(stk2.pop())
    
    return False 
    
    
arr = [1,2,3,4]
testStk = stack()

for x in range(0, len(arr)):
    testStk.push(arr[x])

print(testStk.arr)
print(findTarget(2, testStk))    

    
