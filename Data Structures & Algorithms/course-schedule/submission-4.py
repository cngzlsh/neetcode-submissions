class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True

        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j in prerequisites:
            adjL[i].append(j)

        visiting = set()      # courses on the current path (moved out of the loop)
        visited = set()         # courses already proven safe (new)

        def dfs(i):
            if i in visiting: return False # on the current path: cycle
            if i in visited: return True        # already checked: skip re-exploring (new)
            visiting.add(i)

            for prereq in adjL[i]:
                if not dfs(prereq): 
                    return False
            visiting.remove(i)
            visited.add(i)
            return True
            
        for i in range(numCourses):
            
            if not dfs(i):
                return False

        return True