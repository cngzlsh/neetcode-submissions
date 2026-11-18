class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0, 0
        for p in s:
            if p == '(':
                leftMax += 1
                leftMin += 1
            elif p == ')':
                leftMin = max(0, leftMin - 1)
                leftMax -= 1
                if leftMax < 0: return False
            else:
                leftMin = max(0, leftMin - 1)
                leftMax += 1
            
        if leftMin == 0:
            return True
        else:
            return False