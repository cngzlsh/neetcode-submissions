class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        counter = Counter()
        l = 0
        res = 0
        for r, ch in enumerate(s):
            counter[ch] += 1
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        
        return res
            