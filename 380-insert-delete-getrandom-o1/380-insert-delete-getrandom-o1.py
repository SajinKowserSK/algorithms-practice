from random import random 

class RandomizedSet:

    def __init__(self):
        self.rSet = set() 
        self.len = 0 
        

    def insert(self, val: int) -> bool:
        if val in self.rSet:
            return False 
        
        else:
            self.rSet.add(val)
            self.len += 1 
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.rSet:
            self.rSet.discard(val)
            self.len -= 1 
            return True 
        
        else:
            return False 
            

    def getRandom(self) -> int:
        n = random() * 100 
        n = int(n)
        t = list(self.rSet)
        return t[n%self.len]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()