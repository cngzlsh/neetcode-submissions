class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    dp[0][0] = 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        
        return dp[-1][-1]
