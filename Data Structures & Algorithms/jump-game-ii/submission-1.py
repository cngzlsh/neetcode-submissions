class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        cur = [0]                       # indices reachable with `jumps` jumps
        seen_max = 0                    # farthest index already pushed (avoids re-pushing)
        jumps = 0

        while cur:
            jumps += 1
            nxt = []
            while cur:
                i = cur.pop()
                for j in range(seen_max + 1, min(i + nums[i], n - 1) + 1):
                    if j == n - 1:
                        return jumps
                    nxt.append(j)
                seen_max = max(seen_max, min(i + nums[i], n - 1))
            cur = nxt
        return jumps