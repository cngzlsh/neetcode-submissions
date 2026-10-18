class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backtrack(path, i):
            # i is the number of left brackets
            if i == n :
                while len(path) < 2 * n:
                    path = path + ')'
                results.append(path)
                return
            
            # add left bracket
            path = path + '('
            backtrack(path, i+1)
            path = path[:-1]

            # add right bracket: only possible if left > right
            if i > len(path) - i:
                path = path + ')'
                backtrack(path, i)
                path = path[:-1]
    
        backtrack('(', 1)
        return results