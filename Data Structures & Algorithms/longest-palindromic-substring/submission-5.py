class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = s[0], 1
        for i in range(0, len(s) - 1):
            # odd length
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if resLen < r - l - 1:
                resLen = r - l - 1
                res = s[l+1:r]

            # even length
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if resLen < r - l - 1:
                resLen = r - l - 1
                res = s[l+1:r]
        
        return res