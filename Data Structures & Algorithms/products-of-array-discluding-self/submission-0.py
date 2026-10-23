class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1, n):
            dp1[i] = dp1[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            dp2[j] = dp2[j + 1] * nums[j + 1]
        return [dp1[k] * dp2[k] for k in range(n)]