class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            c = l + (r - l) // 2
            if nums[c] == target:
                return c
            elif nums[c] > target:
                r = c-1
            else:
                l = c+1
        return -1