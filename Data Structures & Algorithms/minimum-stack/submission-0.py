class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefixmin) > 0:
            self.prefixmin.append(min(val, self.prefixmin[-1]))
        else:
            self.prefixmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.prefixmin.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixmin[-1]
        
