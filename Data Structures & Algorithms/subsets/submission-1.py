class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(path, i):
            if i == len(nums):
                res.append(path[:])
                return

            # use
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            # not use
            backtrack(path, i+1)
            return
        
        backtrack([], 0)
        return res