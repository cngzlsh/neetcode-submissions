class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        # keep a total, if total persists to the end of the array, it must be the answer
        res = 0
        total = 0
        
        for i, g in enumerate(gas):
            total += (g - cost[i])
            if total < 0:
                # reset
                res = i + 1
                total = 0
        
        return res