class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        postime = sorted([(position[i], (target - position[i]) / speed[i]) for i in range(len(position))], key=lambda x: -x[0])

        res = 0
        stack = []
        for pos, time in postime:
            if not stack:
                stack.append(time)
            
            else:
                if time > stack[-1]:
                    res += 1
                    stack.pop()
                    stack.append(time)
            
        return res + len(stack)
