class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            
            elif i == len(s):
                return 0
            
            elif (i,j) in dp:
                return dp[(i,j)]
            
            else:
                if s[i] == t[j]:
                    dp[(i,j)] = dfs(i+1, j) + dfs(i+1, j+1)
                    
                
                else:
                    dp[(i,j)] = dfs(i+1, j)
                
                return dp[(i,j)]
        
        
        return dfs(0,0)