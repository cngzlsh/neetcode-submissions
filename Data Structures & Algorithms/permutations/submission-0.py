class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(path):
            if len(path[:]) == len(nums):
                results.append(path[:])
                return
            
            for choice in nums:
                print(choice, path)
                if choice not in path:
                    path.append(choice)
                    backtrack(path)
                    path.pop()
            
        backtrack([])
        return results