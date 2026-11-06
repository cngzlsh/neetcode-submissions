class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    continue
                if r > 0 and c > 0:
                    # can move from down and left
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
        return dp[-1][-1]
