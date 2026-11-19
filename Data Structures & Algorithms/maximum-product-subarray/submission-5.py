class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        res = nums[0]
        cur_min, cur_max = 1, 1
        for num in nums:
            candidates = (num, cur_max * num, cur_min * num)
            cur_max, cur_min = max(candidates), min(candidates)
            res = max(res, cur_max)
        return res