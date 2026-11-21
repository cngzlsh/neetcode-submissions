class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        _max = 1

        def dfs(i,j):
            nonlocal _max
            if (i, j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = 1
            for dx, dy in ([0,1], [0,-1], [1,0], [-1,0]):
                nx, ny = i + dx, j + dy
                
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[i][j]:
                    dp[(i,j)] = max(dp[(i,j)], 1 + dfs(nx, ny))
                    _max = max(_max, dp[(i,j)])
            
            return dp[(i,j)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j)
        
        return _max


