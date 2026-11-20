class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(path, i):
            if i == len(nums):
                res.add(tuple(sorted(path[:])))
                return
            
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            backtrack(path, i+1)

        backtrack([], 0)
        return [list(x) for x in res]