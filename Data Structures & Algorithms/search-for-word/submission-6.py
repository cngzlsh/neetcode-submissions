class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        rows, cols = len(board), len(board[0])

        def backtrack(x, y, i):
            if i==n:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if board[nx][ny] == word[i]:
                        visited.add((nx, ny))
                        if backtrack(nx, ny, i+1): 
                            return True
                        visited.remove((nx, ny))
                
            return False
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r,c))
                    if backtrack(r, c, 1): return True
        
        return False
            
