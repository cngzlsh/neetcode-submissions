class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjL = {ch: set() for w in words for ch in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjL[w1[j]].add(w2[j])
                    break
        
        # post order dfs
        visited = set()
        visiting = set()
        order = []
        def dfs(ch):
            if ch in visited: return True
            if ch in visiting: return False
            visiting.add(ch)
            for child in adjL[ch]:
                if not dfs(child): return False
            
            visited.add(ch)
            visiting.remove(ch)
            order.append(ch)
            return True
        
        for ch in adjL:
            if not dfs(ch): return ""
        
        return ''.join(order)[::-1]