class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:        # only start at the beginning of a run
                length = 1
                while n + length in nums:
                    length += 1
                res = max(res, length)
        return res