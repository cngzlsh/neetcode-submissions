class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, rest = float('-inf'), 0, 0
        for p in prices:
            prev_sold = sold
            sold = hold + p                  # sell today (uses yesterday's hold)
            hold = max(hold, rest - p)       # keep holding, or buy from a rest day
            rest = max(rest, prev_sold)      # do nothing, or finish yesterday's cooldown
        return max(sold, rest)
