class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True

        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j in prerequisites:
            adjL[i].append(j)

        visiting = set()
        visited = set()

        def dfs(i):
            if i in visiting: return False
            if i in visited: return True
            if not adjL[i]: return True
            visiting.add(i)

            for neig in adjL[i]:
                if not dfs(neig): return False
            
            visiting.remove(i)
            visited.add(i)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): return False
        
        return True
            
            