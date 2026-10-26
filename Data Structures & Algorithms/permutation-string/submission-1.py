from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        need = Counter(s1)
        window = Counter(s2[:n])
        if window == need:
            return True
        for r in range(n, m):
            window[s2[r]] += 1             # letter entering
            window[s2[r - n]] -= 1         # letter leaving
            if window[s2[r - n]] == 0:
                del window[s2[r - n]]      # so Counter equality works
            if window == need:
                return True
        return False