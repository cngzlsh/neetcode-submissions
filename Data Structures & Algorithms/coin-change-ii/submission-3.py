class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 2d dp: dp[(i,s)] is the number of ways from s to get to amount with coin i or more
        coins.sort()
        dp = {}

        def dfs(i, s):
            if (i,s) in dp:
                return dp[(i, s)]
            if s == amount:
                return 1
            if s > amount:
                return 0
            
            res = 0
            for coin in coins:
                if coin < i:
                    continue
                res += dfs(coin, s+coin)
            
            dp[(i, s)] = res
            return res

        return dfs(coins[0], 0)