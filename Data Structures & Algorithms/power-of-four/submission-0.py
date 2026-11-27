class Solution:
    def isPowerOfFour(self, n: int) -> bool:


        while n!= 1:
            if n!= 0 and n % 4 == 0:
                n /= 4
            else:
                return False
        
        return True