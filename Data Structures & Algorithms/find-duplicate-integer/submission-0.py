class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for n in nums:
            if n not in visited:
                visited.add(n)
            else:
                return n