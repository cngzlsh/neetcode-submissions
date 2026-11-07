class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {} #(t, c) = number of ways to get to amount t if using coins with face values c or more

        def dfs(total, c):
            if total == amount:
                return 1
            if total > amount:
                return 0
            
            if (total, c) in dp:
                return dp[(total, c)]

            dp[(total, c)] = 0
            for coin in coins:
                if coin >= c:
                    dp[(total, c)] += dfs(total+coin, coin)
            
            return dp[(total, c)]
        
        return dfs(0, coins[0])