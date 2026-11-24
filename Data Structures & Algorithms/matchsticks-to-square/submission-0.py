class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4: return False
        side = total // 4
        if max(matchsticks) > side: return False
        
        def backtrack(used, curr_sum):
            if curr_sum == side:
                curr_sum = 0

            if len(used) == len(matchsticks):
                return True
            
            for i in range(len(matchsticks)):
                if i not in used and curr_sum + matchsticks[i] <= side:
                    used.add(i)
                    if backtrack(used, curr_sum + matchsticks[i]):
                        return True
                    used.remove(i)
            
            return False
        
        return backtrack(set(), 0)