class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        def backtrack(path, idxs):
            if len(path) == len(nums):
                res.add(tuple(path[:]))
                return
            
            for i in range(len(nums)):
                if i not in idxs:
                    path.append(nums[i])
                    idxs.add(i)
                    backtrack(path, idxs)
                    path.pop(-1)
                    idxs.remove(i)
            
        backtrack([], set())
        return [list(x) for x in res]