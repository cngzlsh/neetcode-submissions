class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)

        res = 0
        single_in_the_middle = False
        for ch in count:
            if count[ch] % 2 == 0:
                res += count[ch]
            else:
                res += count[ch] - 1
                single_in_the_middle = True
        
        if single_in_the_middle:
            return res + 1
        else:
            return res