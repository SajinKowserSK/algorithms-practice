class Solution(object):
    class Stack:
        def __init__(self):
            self.stack = []

        def isEmpty(self):
            return len(self.stack) == 0

        # adds to front bc LIFO
        def push(self, item):
            self.stack.insert(0, item)

        def pop(self):
            if len(self.stack) > 0:
                front = self.stack[0]
                self.stack.remove(front)
                return front
            else:
                return None

        def peek(self):
            if len(self.stack) == 0:
                return None

            else:
                return self.stack[0]
            
       
                
    def isValid(self, s):
        myMap = {}
        myMap['('] = ')'
        myMap[')'] = '('
        myMap['['] = ']'
        myMap[']'] = '['
        myMap['{'] = '}'
        myMap['}'] = '{'
        
        stk1 = self.Stack()
        stk2 = self.Stack()
        
        if len(s) % 2 != 0:
            return False 

        for x in range (len(s)-1, -1, -1):

            stk1.push(s[x])
        
        
        while stk1.isEmpty() == False:
            top = stk1.peek()
            if top == '(' or top == '{' or top == '[':
                stk2.push(stk1.pop())
                
            else: # closing brace
                if stk2.isEmpty() == False:
                    top2 = stk2.peek()
                    if top == myMap[top2]:
                        stk1.pop()
                        stk2.pop()

                    else:
                        return False 
                    
                else:
                    return False 
 
        if stk2.isEmpty():
            return True
        
        else:
            return False 
        

            
        
        
        
        