class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, i, s):
            if s == target:
                res.append(path[:])
            if s > target:
                return
            
            for j, choice in enumerate(nums):

                if j < i: 
                    continue

                path.append(choice)
                backtrack(path, j, s + choice)
                path.pop()
            
            return
        
        backtrack([], 0, 0)
        return res