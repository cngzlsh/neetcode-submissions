class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = max subarray ending i, regardless of how it was earlier
        dp = [None] * len(nums)

        for i, n in enumerate(nums):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1] + n, n)
        
        return max(dp)