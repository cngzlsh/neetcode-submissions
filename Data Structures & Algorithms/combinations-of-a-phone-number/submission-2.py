class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letters = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        results =[]
        def backtrack(i, path):
            if i == len(digits):
                results.append(''.join(path[:]))
                return
            
            for l in letters[digits[i]]:
                path.append(l)
                backtrack(i+1, path)
                path.pop()
            
        backtrack(0, [])
        return results