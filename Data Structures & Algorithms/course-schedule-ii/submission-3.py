class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        adjL = defaultdict(list)
        for i, j in prerequisites:
            adjL[i].append(j)
        res = []
        
        visiting, visited = set(), set()
        def dfs(i):
            if i in visited:
                return True
            
            if i in visiting:
                return False
            
            visiting.add(i)
            for ch in adjL[i]:
                if not dfs(ch): return False
            
            visiting.remove(i)
            visited.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res