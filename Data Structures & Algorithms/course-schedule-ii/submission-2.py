class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j in prerequisites:
            adjL[i].append(j)

        visiting = set()
        visited = set()
        order = []
        

        def dfs(i):
            if i in visiting: return False
            if i in visited: return True
            visiting.add(i)

            for neig in adjL[i]:
                if not dfs(neig): return False
            
            visiting.remove(i)
            visited.add(i)
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return order