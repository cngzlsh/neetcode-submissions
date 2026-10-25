class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy: only keep farthest position
        farthest = 0
        for i, n in enumerate(nums):
            if i > farthest: 
                return False

            farthest = max(farthest, i + n)
            if farthest >= len(nums) - 1: 
                return True
        
        return False