class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n not in visited:
                visited.add(n)
            else:
                return True
        return False