#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] 最大矩形
# 思路：基于84题，把本题的每一行极其上部看作一个个柱子，就可以按照84题实现。

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left, right = [0]*n, [0]*n
        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n-1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        maxare = 0
        for i in range(row):
            for j in range(col):
                heights[j] = (heights[j] + int(matrix[i][j])) if matrix[i][j] == '1' else 0
            maxare = max(maxare, self.largestRectangleArea(heights))
        return maxare

# @lc code=end

