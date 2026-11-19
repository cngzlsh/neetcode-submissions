class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[(i,j)] is the edit distance between word1[i:] and word2[j:]
        dp = {}

        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                dp[(i,j)] = 0
                return 0

            if i == len(word1):
                dp[(i,j)] = len(word2) - j
            if j == len(word2):
                dp[(i,j)] = len(word1) - i
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            
            else:
                insert = 1 + dfs(i, j+1)
                delete = 1 + dfs(i+1,j)
                replace = 1 + dfs(i+1,j+1)
                dp[(i,j)] = min([insert, delete, replace])
            
            return dp[(i,j)]
        
        return dfs(0,0)