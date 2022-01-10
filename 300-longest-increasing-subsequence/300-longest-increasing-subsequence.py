class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        
        # O(N^2) soln with cacheing 
        # set all elems dp[x] = 1
        # iterate i from end of list - 1 to front,
            # iterate n from i -> end of list 
            # if list[n] >= list[i], dp[i] = dp[list[n]] + 1
            
        
        for elem in nums:       
            dp[elem] = 1 
      
        for i in range(len(nums)-2, -1, -1):
            
            for n in range(i+1, len(nums)):
                if nums[i] < nums[n]:
                    dp[nums[i]] = max(dp[nums[i]], 1 + dp[nums[n]])

                    
 
        longest = float("-inf")
        for key in dp:
            longest = max(dp[key], longest)
        return longest 
                
                        
                    
            
            
        