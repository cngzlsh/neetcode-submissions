class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n - 1):                 # size of the window
            for l in range(1, n - length):
                r = l + length - 1
                best = 0
                for i in range(l, r + 1):              # i is the LAST balloon burst
                    best = max(best,
                               dp[l][i-1] + nums[l-1] * nums[i] * nums[r+1] + dp[i+1][r])
                dp[l][r] = best
        return dp[1][n - 2]