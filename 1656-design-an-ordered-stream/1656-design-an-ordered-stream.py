class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["-1" for x in range(n)] 
        self.ptr = 0 
        self.chunks = []

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        currChunk = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] != "-1":
            currChunk.append(self.stream[self.ptr])
            self.ptr += 1 
            
        self.chunks.append(currChunk)
        return currChunk 
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)