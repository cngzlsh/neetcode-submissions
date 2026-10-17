class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ['(','{','[']:
                stack.append(p)
            elif not stack:
                return False
            elif p == ')' and stack[-1] == '(':
                stack.pop()
            elif p == '}' and stack[-1] == '{':
                stack.pop()
            elif p == ']' and stack[-1] == '[':
                stack.pop()  
            else:
                return False
        if not stack:
            return True
        return False