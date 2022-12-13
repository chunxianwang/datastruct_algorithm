#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
# 总体思路：枚举每个柱子（height），计算以它为高，宽度为左右两侧某边界的矩形面积，然后在所有矩形面积中求最小值。
# 重点是如何对每个柱子（height）求左右边界：
#     左边界是在左侧且最近的小于其高度的柱子，
#     右侧边界就是在右侧且最近的小于其高度的柱子。




# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left, right = [0]*n, [0]*n
        mono_stack = list() #单调栈：存放单调递增柱子的位置
        for i in range(n):
            # 已入栈柱子与当前待入栈柱子比较高度，如果已入栈柱子高度较大，把它从栈中弹出
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
        
        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n > 0 else 0
        return ans




# @lc code=end

