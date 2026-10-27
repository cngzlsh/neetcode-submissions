class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        p = 1

        for i in range(1, n+1):
            if i == p * 2:
                p *= 2
                dp[p] = 1
            else:
                dp[i] = 1 + dp[i-p]
        
        return dp