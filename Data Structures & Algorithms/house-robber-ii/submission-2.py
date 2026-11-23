class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        # dp1 starts from index 0
        # dp2 starts from index 1
        dp1, dp2 = [0, nums[0]], [0, nums[1]]

        for i in range(1, len(nums) - 1):
            dp1.append(max(dp1[-2]+nums[i], dp1[-1]))
            dp2.append(max(dp2[-2]+nums[i+1], dp2[-1]))
        
        return max(dp1[-1], dp2[-1])