class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        adjL = defaultdict(list)
        for cor, pre in prerequisites:
            adjL[cor].append(pre)
        
        # topological sort: need to keep both visiting and visited
        visited = set()
        visiting = set()
        def dfs(c):
            if c in visited: return True
            if c in visiting: return False

            visiting.add(c)
            for pre in adjL[c]:
                if not dfs(pre): 
                    return False
            
            visiting.remove(c)
            visited.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True
            