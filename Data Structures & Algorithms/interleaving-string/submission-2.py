class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3): return False

        if not s1: return s3 == s2
        if not s2: return s3 == s1
        dp = {}

        def dfs(i, j):
            
            if i == l1 and j == l2:
                return True
            if i > l1 or j > l2:
                return False
            

            if i == l1:
                si=s1[-1]
            else:
                si = s1[i]
            if j == l2:
                sj = s2[-1]
            else:
                sj = s2[j]
            
            
            if (i, j) in dp: return dp[(i,j)]
            
            if s3[i+j] == si and s3[i+j] != sj:
                
                dp[(i,j)] = dfs(i+1, j)

                return dp[(i,j)]
            elif s3[i+j] != si and s3[i+j] == sj:
                dp[(i,j)] = dfs(i, j+1)
                return dp[(i,j)]
            
            elif s3[i+j] == si and s3[i+j] == sj:
                dp[(i,j)] = dfs(i+1, j) or dfs(i, j+1)
                return dp[(i,j)]

            elif s3[i+j] != si and s3[i+j] != sj:
                dp[(i,j)] = False
                return False
        
        return dfs(0,0)
        
