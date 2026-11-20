class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        for x in range(1, len(nums) + 2):
            if x not in seen:
                return x