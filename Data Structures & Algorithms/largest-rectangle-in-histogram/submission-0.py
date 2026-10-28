class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for curr_i, curr_h in enumerate(heights):
            if not stack:
                stack.append([curr_i, curr_h])
            
            else:
                if curr_h >= stack[-1][1]:
                    stack.append([curr_i, curr_h])
                else:
                    while stack and stack[-1][1] > curr_h:
                        i, h = stack.pop()
                        maxArea = max(maxArea, h * (curr_i - i))
                        start = i
                    stack.append([start, curr_h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea