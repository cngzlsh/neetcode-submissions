class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n^2) solution: matrix n x n, fill with product from i to j, take max
        # O(n): Kadane's algorithm
        cur_max = cur_min = best = nums[0]
        for x in nums[1:]:
            candidates = (x, cur_max * x, cur_min * x)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best
