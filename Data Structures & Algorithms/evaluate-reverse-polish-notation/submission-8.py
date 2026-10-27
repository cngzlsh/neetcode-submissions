class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+/*-':
                stack.append(int(t))
            else:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if t == '+':
                    stack.append(n1 + n2)
                elif t == '/':
                    stack.append(int(n2 / n1))
                elif t == '-':
                    stack.append(n2 - n1)
                else:
                    stack.append(n1 * n2)
        return stack[0]