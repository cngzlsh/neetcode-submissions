class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(path, i):
            if i >= len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(path, j + 1)
                    path.pop()

        backtrack([], 0)
        return res

    def isPalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True