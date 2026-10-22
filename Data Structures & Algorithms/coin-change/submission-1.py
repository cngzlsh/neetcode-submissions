class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is thenumber of ways to get to amount i
        # let dp[0] be amount 0 as a dummy
        dp = [-1 for _ in range(amount +1)]
        dp[0] = 0
        for i in range(1, amount+1):
            _min = float('inf')
            for c in coins:
                
                if i-c >= 0:
                    _min = min(_min, dp[i-c] + 1)
                dp[i] = _min
        
        print(dp)
        return -1 if dp[-1] == float('inf') else dp[-1]