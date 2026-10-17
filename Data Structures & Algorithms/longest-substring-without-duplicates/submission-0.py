class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {} # store string -> last seen index
        l = 0
        maxLen = 0
        for r, ch in enumerate(s):
            
            if ch  in visited:
                l = max(l, visited[ch] + 1)
            visited[ch] = r
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen