class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        res = ''
        n = len(s)
        if n == 1: return s

        for i in range(n):
            # case 1: odd length
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if maxL < r - l + 1:
                    maxL = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1
            
            # case 2: even number
            l , r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if maxL < r - l + 1:
                    maxL = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1
            
        
        return res