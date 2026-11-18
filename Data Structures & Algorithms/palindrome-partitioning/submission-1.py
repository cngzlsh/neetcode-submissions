class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, path):
            if i >= len(s):
                res.append(path[:])
            
            for j in range(i+1, len(s) + 1):
                if isPalin(s[i:j]):
                    path.append(s[i:j])
                    backtrack(j, path)
                    path.pop()
        
            return
        
        def isPalin(k):
            if len(k) % 2 == 0:
                l, r = len(k) // 2 - 1, len(k) // 2
                while l >= 0 and r <=len(k) - 1:
                    if k[l] != k[r]: return False
                    l -= 1
                    r += 1
            else:
                l, r = len(k) // 2, len(k) // 2
                while l >= 0 and r <=len(k) - 1:
                    if k[l] != k[r]: return False
                    l -= 1
                    r += 1
            
            return True
        
        backtrack(0, [])
        return res