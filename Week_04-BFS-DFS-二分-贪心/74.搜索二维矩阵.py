#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            pivotindex = (left + right) // 2
            pivotelement = matrix[pivotindex//n][pivotindex % n]
            if target == pivotelement:
                return True
            if target < pivotelement:
                right = pivotindex - 1
            else:
                left = pivotindex + 1
        return False

# @lc code=end

