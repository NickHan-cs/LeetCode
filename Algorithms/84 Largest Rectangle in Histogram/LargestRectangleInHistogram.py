class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        minIdx, maxIdx, stack = [-1] * l, [l] * l, []
        for i in range(l):
            while stack and heights[stack[-1]] >= heights[i]:
                maxIdx[stack[-1]] = i
                stack.pop()
            minIdx[i] = stack[-1] if stack else -1
            stack.append(i)
        return max((maxIdx[i] - minIdx[i] - 1) * heights[i] for i in range(l)) if l > 0 else 0