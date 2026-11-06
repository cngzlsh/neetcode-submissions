class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1: return dp[0]
        dp[1] = nums[1]
        if len(nums) == 2: return max(dp)
        dp[2] = nums[0] + nums[2]
        if len(nums) == 3: return max(dp[1], dp[2])

        for i in range(3, len(dp)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
        return max(dp[-1], dp[-2])

            