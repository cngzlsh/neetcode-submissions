class Solution:
    def numDecodings(self, s: str) -> int:
        # at idx i, there are two states, if it's a single number (1) or if it binds with the prev (2)
        dp = {(i, 1):0 for i in range(len(s))} | {(i, 2):0 for i in range(len(s))}
        
        for i, num in enumerate(s):
            if i == 0:
                if num == '0': 
                    return 0
                else:
                    dp[(i, 1)] = 1
                    continue
            
            if num == '0':
                if int(s[i-1] + '0') >= 30: 
                    return 0
                else:
                    dp[(i, 2)] = dp[(i-1, 1)]
                    dp[(i, 1)] = 0
            else:
                if int(s[i-1] + num) <= 26:
                    dp[(i, 1)] = dp[(i-1, 1)] + dp[(i-1, 2)]
                    dp[(i, 2)] = dp[(i-1, 1)]
                else:
                    dp[(i, 1)] = dp[(i-1, 1)] + dp[(i-1, 2)]
                    dp[(i, 2)] = 0
        
        return dp[(len(s)-1, 1)] + dp[(len(s)-1, 2)]
