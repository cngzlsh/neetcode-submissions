class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[(i, s)] = number of ways at ith index to sum to 
        dp = {}
        res = 0

        def dfs(i, s):
            if i == len(nums):
                return 1 if s == target else 0

            if (i, s) in dp: return dp[(i,s)]
            
            dp[(i, s)] = dfs(i+1, s+nums[i]) + dfs(i+1, s-nums[i])
            return dp[(i, s)]

        return dfs(0,0)