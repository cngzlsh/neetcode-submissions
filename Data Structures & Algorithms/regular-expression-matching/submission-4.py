class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ls, lp = len(s), len(p)

        # top-down dp
        # dp = {}

        # def dfs(i, j):
        #     if i == ls - 1 and j == lp - 1:
        #         if s[i] == p[j] or p == '.' or p == '*':
        #             return True
        #         else:
        #             return False

        #     if (i, j) in dp: 
        #         return dp[(i,j)]
            
        #     if p[j] not in ['.', '*']:

        # bottom up dp, ficticious row and column at the end and empty string matches empty string
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[-1][-1] = True          # empty s matches empty p

        for i in range(ls, -1, -1):             # include i == ls (empty s)
            for j in range(lp - 1, -1, -1):
                first = i < ls and (p[j] == s[i] or p[j] == '.')

                if j + 1 < lp and p[j + 1] == '*':
                    # zero copies of p[j]  OR  one copy, then stay on j
                    dp[i][j] = dp[i][j + 2] or (first and dp[i + 1][j])
                else:
                    dp[i][j] = first and dp[i + 1][j + 1]

        return dp[0][0]
