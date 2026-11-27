class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):                 # new: keeps s3[i+j] in range
            return False

        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == l1 and j == l2:
                return True

            m1 = i < l1 and s1[i] == s3[i + j]    # new: bounds-safe match flags
            m2 = j < l2 and s2[j] == s3[i + j]

            if m1 and not m2:
                dp[(i, j)] = dfs(i + 1, j)
            elif m2 and not m1:
                dp[(i, j)] = dfs(i, j + 1)
            elif m1 and m2:
                dp[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
            else:
                dp[(i, j)] = False                # new: neither matches, dead end

            return dp[(i, j)]

        return dfs(0, 0)