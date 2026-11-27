class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        if n == 1: return 1

        for i in range(n):
            # case 1: odd length
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1

                l -= 1
                r += 1
            
            # case 2: even number
            l , r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1

                l -= 1
                r += 1
            
        
        return res