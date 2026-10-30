class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[i][j] is the longest increasing path from that point onwards.
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        dp = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(i, j):
            if (i,j) in dp: return dp[(i,j)]

            curr = matrix[i][j]
            dp[(i,j)] = 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > curr:
                    dp[(i,j)] = max(dp[(i,j)], 1 + dfs(ni, nj))
            
            return dp[(i,j)]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        
        return max(dp.values())