class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        s = s // 2
        dp = {}

        def dfs(i, curr_s):
            if curr_s == s: return True
            if i == len(nums): return False

            if (i, curr_s) in dp: return dp[(i, curr_s)]

            dp[(i, curr_s)] = dfs(i + 1, curr_s) or dfs(i + 1, curr_s + nums[i])

            return dp[(i, curr_s)]
        
        return dfs(0,0)