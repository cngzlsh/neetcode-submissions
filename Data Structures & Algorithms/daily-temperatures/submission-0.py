class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped, j = stack.pop()
                res[j] = i- j
                
            stack.append((temp, i))

        return res