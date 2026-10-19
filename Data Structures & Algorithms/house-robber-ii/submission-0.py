class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        # split into 2 cases
        # if house 1 robbed, house n not robbed
        
        dp = [0 for _ in range(len(nums)-1)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        for i in range(3, len(nums)-1):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        case1 = max(dp[-1], dp[-2])

        # if house 1 not robbed, house n robbed

        dp = [0 for _ in range(len(nums)-1)]
        dp[0] = nums[1]
        dp[1] = nums[2]
        dp[2] = nums[1] + nums[3]
        for i in range(3, len(nums)-1):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i+1]
        case2 = max(dp[-1], dp[-2])

        return max(case1, case2)