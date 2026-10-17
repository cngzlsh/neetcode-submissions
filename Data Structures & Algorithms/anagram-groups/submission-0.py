class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            letters = tuple(sorted(k for k in word))
            if letters not in h:
                h[letters] = [word]
            else:
                h[letters].append(word)
        
        return list(h.values())