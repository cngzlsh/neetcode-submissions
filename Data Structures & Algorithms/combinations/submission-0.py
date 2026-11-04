class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(path, start):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(start, n+1):
                path.append(j)
                backtrack(path, j+1)
                path.pop()
        
            return
        
        backtrack([], 1)
        return res