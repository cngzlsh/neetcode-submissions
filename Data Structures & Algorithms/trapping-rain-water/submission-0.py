class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        curLvl = min(maxL, maxR)
        res = curLvl * (r - l - 1)

        while l + 1 < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                newLvl = min(maxL, maxR)
                res += (newLvl - curLvl) * (r - l - 1)   # raise level for the remaining interior
                res -= min(curLvl, height[l])            # column l leaves the interior at the old level
            else:
                r -= 1
                maxR = max(maxR, height[r])
                newLvl = min(maxL, maxR)
                res += (newLvl - curLvl) * (r - l - 1)
                res -= min(curLvl, height[r])
            curLvl = newLvl
        return res