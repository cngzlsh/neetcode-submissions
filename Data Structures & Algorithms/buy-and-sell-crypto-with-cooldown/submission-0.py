class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # There are two states: buying and selling
        # if buy: i + 1
        # if sell: i + 2

        dp = {} # key=(i, buying), key = max profit 

        def dfs(i, buying): # buying here is a booling
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                # can buy
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # can sell
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)