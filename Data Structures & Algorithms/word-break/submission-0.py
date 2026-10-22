class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp: dp[n] is whether dp[n:] can be matched with words in wordDict
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= n and dp[i+len(word)] and s[i:i+len(word)] == word:
                    dp[i] = True
        
        return dp[0]