class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(path, l, r):
            if l == r == n:
                res.append(''.join(path[:]))
                return
            
            if l > n or r > n:
                return
            
            if l > r:
                # add (
                path.append('(')
                backtrack(path, l+1, r)
                path.pop()
                # add )
                path.append(')')
                backtrack(path, l, r+1)
                path.pop()
            
            else:
                # equal number of left and right brackets, can only add left
                path.append('(')
                backtrack(path, l+1, r)
                path.pop()
        
        backtrack([], 0, 0)
        return res           