class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = min(heights[l], heights[r]) * ( r- l)

        while l < r:
            if heights[l] < heights[r]:
                # move left
                l += 1
            else:
                r -= 1
            res = max(res, min(heights[l], heights[r]) * ( r- l))

        return res
