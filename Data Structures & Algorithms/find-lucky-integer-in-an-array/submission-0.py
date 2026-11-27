class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        count = Counter(arr)
        res = -1
        for n in count:
            if count[n] == n:
                res = max(res, n)
        
        return res