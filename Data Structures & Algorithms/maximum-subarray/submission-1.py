class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        best = float('-inf')
        for n in nums:
            prefix += n
            best = max(best, prefix - min_prefix)
            min_prefix = min(prefix, min_prefix)
        return best