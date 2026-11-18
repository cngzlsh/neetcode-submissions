class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if target == 0: return 1

        time = []
        for i, pos in enumerate(position):
            time.append([pos, (target-pos) / speed[i]])
        time.sort(key=lambda x: x[0])

        res = 1
        curr_time = time[-1][1]
        while time: 
            _, t = time.pop()
            if t > curr_time:
                res += 1
                curr_time = t
        
        return res