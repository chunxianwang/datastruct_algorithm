#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        for j in range(1, row):
            grid[j][0] += grid[j-1][0]
        for i in range (1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][col-1]


# @lc code=end

