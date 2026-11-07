class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        output = []
        q = deque()
        l = r = 0

        # queue holds LEFT: maxmimum element's INDEX in the sliding window -> RIGHT smaller element's INDEX since maximum element
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                # if new incoming value is greater than the right end, pop them
                q.pop()
            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output