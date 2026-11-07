class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # [day, state] -> max

        def dfs(i, bought):
            if (i, bought) in dp:
                return dp[(i, bought)]
            
            if i >= len(prices):
                return 0
            
            # not bought:
            if not bought:
                hold = dfs(i+1, False)
                buy = dfs(i+1, True) - prices[i]
                dp[(i, False)] = max(hold, buy)
                return dp[(i, False)]

            # bought
            if bought:
                hold = dfs(i+1, True)
                sell = dfs(i+2, False) + prices[i]
                dp[(i, True)] = max(hold, sell)
            
                return dp[(i, True)]
        
        return dfs(0, False)
