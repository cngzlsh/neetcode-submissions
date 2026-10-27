class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        twos = [1]
        k = 0
        while 2 **k <= n:
            k += 1
            twos.append(2 ** k)
           

        for i in range(1, n+1):
            if i in twos:
                dp[i] = 1
            else:
                # largest power of 2
                for k, p in enumerate(twos):
                    if p > i:
                        break
                dp[i] = 1 + dp[i - twos[k-1]]
        
        return dp