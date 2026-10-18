class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2D DP: dp[i][j] = number of matched characters so far in s[:i] and t[:j]
        m, n = len(s), len(t)
        if m == 0: return True
        if n == 0: return False
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if dp[i][j] == m:
                    return True
        
        return False