#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
#从右上角开始，往左下放，不断缩小搜索空间，知道找到target
# 若当前行最后的一个元素大于target，则查询向左移动，即列数减少一，
# 若当前行的最后一个值小于target，则行数向下增加，即行数加一。
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix[0]) - 1
        if len(matrix) == 0: return False
        while col >=0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            if matrix[row][col] < target:
                row += 1
        return False

# @lc code=end

