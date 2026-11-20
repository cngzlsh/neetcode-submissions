class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        return [val for val, cnt in Counter(nums).items() if cnt > n // 3]