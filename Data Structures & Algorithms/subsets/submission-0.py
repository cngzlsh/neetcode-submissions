class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []

        def backtrack(path, level):
            # end position:
            if level == n:
                results.append(path[:])
                return
            
            # choose
            path.append(nums[level])
            backtrack(path, level+1)
            path.pop()

            # not choose
            backtrack(path, level+1)
        
        backtrack([], 0)

        return results