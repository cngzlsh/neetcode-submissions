class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        l = res = 0
        for r, ch in enumerate(s):
            if ch in last:
                l = max(l, last[ch] + 1)
            last[ch] = r
            res = max(res, r - l + 1)
        return res