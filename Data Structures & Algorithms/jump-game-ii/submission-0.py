class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[0] = 0
        for i, n in enumerate(nums):
            for j in range(0, n):
                if i+j+1 < len(nums):
                    dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)
        
        return dp[-1]