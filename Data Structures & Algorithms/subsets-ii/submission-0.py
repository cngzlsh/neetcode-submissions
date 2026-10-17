class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = set()
        def backtrack(path, level):
            if level == len(nums):
                results.add(tuple(sorted(path)))
                return
            
            path.append(nums[level])
            backtrack(path, level+1)
            path.pop()

            backtrack(path, level+1)
        
        backtrack([], 0)
        return [list(t) for t in results]
