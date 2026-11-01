class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        
        if not digits: return []

        res = []
        def backtrack(i, path):
            if i == len(digits):
                res.append(path[:])
                return
            
            for ch in d[digits[i]]:
                path += ch
                backtrack(i+1, path)
                path = path[:-1]
        
        backtrack(0, '')
        return res