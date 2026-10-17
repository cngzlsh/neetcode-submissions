class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(comb, s, i):
            if s == target:
                results.append(comb[:])
                return
            elif s > target:
                return
            
            for j, choice in enumerate(nums):
                if j < i:
                    continue
                comb.append(choice)
                backtrack(comb, s=s+choice, i=j)
                comb.pop()
        
        backtrack([], 0, 0)

        return results