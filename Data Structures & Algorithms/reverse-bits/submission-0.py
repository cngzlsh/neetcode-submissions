class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, '032b') 
        res = 0
        for i, b in enumerate(n):
            if b == '1':
                res += 2 ** i
        
        return res