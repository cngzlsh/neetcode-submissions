class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = float('inf')
        maxProf = 0
        for p in prices:
            if p > minsofar:
                maxProf = max(maxProf, p - minsofar)
            minsofar = min(minsofar, p)
        return maxProf
