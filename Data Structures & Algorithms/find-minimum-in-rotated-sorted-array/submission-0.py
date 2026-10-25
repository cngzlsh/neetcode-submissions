class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                # minimum in right
                l = m + 1
            else:
                # minimum in left
                r = m

        return nums[l]