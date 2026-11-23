class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjL = {}

        for orig, dest in tickets:
            if orig not in adjL:
                adjL[orig] = [dest]
            else:
                adjL[orig].append(dest)
        
        for orig in adjL:
            adjL[orig] = sorted(adjL[orig])
        
        result = None
        def dfs(orig, path):
            nonlocal result
            if not adjL:
                result = path[:]
                return True
            
            if orig not in adjL:
                return False
            
            for i, dest in enumerate(adjL[orig]):
                adjL[orig].pop(i)
                if not adjL[orig]:
                    del adjL[orig]

                path.append(dest)
                if dfs(dest, path): 
                    return True
                
                path.pop()
                if orig not in adjL:
                    adjL[orig] = [dest]
                else:
                    adjL[orig].insert(i, dest)
            return False
        
        dfs('JFK', ['JFK'])
        return result




            
            
