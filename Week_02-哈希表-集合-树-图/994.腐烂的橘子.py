#
# @lc app=leetcode.cn id=994 lang=python
#
# [994] 腐烂的橘子
#
import collections

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 广度优先搜索
        nr = len(grid)
        nc = len(grid[0])
        directions = {(-1, 0), (1, 0), (0, -1), (0,1)}
        queue = collections.deque()
        count_1 = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    count_1 += 1
        if count_1 == 0: return 0
        if not queue: return -1
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row>=0 and row < nr and col >=0 and col < nc and grid[r+dr][c+dc] == 1:
                    grid[row][col] = 2
                    queue.append((row, col, d + 1))
        if any(1 in row for row in grid):
            return -1
        return d
# @lc code=end

