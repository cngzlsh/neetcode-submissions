class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        if len(s1) > len(s2): return False

        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == need:
            return True
        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            window[s2[r-len(s1)]] -= 1
            if window[s2[r-len(s1)]] == 0:
                del window[s2[r-len(s1)]] 
            if window == need:
                return True
        
        return False
            
            