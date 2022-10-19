class Solution:

    def __init__(self, w: List[int]):
        # need to first create a cumulative sum form 
        # then also store the total

        # get a random number from 1 to the total
        # iterate through linearly and get the first index that's > than the random number 

        # [1, 3] -> prefix sum is [1, 4] & total is 4 -> randint (1, 4) -> 1/4 of idx 1 and 2,3,4(3)/4 of getting idx 1
        self.prefixSums = [] 
        self.total = 0 

        for weight in w: 
            self.total += weight 
            self.prefixSums.append(self.total)
        
    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        low, high = 0, len(self.prefixSums)
        while low < high:
            mid = low + (high - low) // 2

            # the target amount needs a higher range
            if target > self.prefixSums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()