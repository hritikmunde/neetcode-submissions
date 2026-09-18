class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                right = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, width * heights[right])
            stack.append(i)
        while stack:
            right = stack.pop()
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            max_area = max(max_area, width * heights[right])
        return max_area