#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, r, c):
            nr = len(grid)
            nc = len(grid[0])
            grid[r][c] = '0'
            if r-1>=0 and grid[r-1][c] == '1': dfs(grid, r-1, c)
            if r+1<nr and grid[r+1][c] == '1': dfs(grid, r+1, c)
            if c-1>=0 and grid[r][c-1] == '1': dfs(grid, r, c-1)
            if c+1<nc and grid[r][c+1] == '1': dfs(grid, r, c+1)

        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_island += 1
                    dfs(grid, r, c)
        return num_island
# @lc code=end

