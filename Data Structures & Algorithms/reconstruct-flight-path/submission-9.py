class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjL = {}

        for orig, dest in tickets:
            if orig not in adjL:
                adjL[orig] = [dest]
            else:
                adjL[orig].append(dest)
        
        for orig in adjL:
            adjL[orig] = sorted(adjL[orig], reverse=True)
        
        result = []
        def dfs(orig):
            while adjL.get(orig):
                dfs(adjL[orig].pop())
            result.append(orig)
        
        dfs('JFK')
        return result[::-1]




            
            
