#
# @lc app=leetcode.cn id=695 lang=python
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        # 深度优先
        def dfs(grid, r, c):
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            ans = 1
            ans += dfs(grid, r-1, c)
            ans += dfs(grid, r+1, c)
            ans += dfs(grid, r, c-1)
            ans += dfs(grid, r, c+1)
            return ans

        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        maxArea = 0
        for r in range(nr):
            for c in range(nc):
                maxArea = max(maxArea, dfs(grid, r, c))
        return maxArea
        '''
        
        # 广度优先
        
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        maxArea = 0
        directions = {(-1, 0), (1,0), (0,-1), (0,1)}
        queue = collections.deque()
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]:
                    queue.append((r, c))
                    grid[r][c] = 0
                    count = 1
                    while queue:
                        point = queue.popleft()
                        for direction in directions:
                            row = point[0] + direction[0]
                            col = point[1] + direction[1]
                            if row>=0 and row < nr and col>= 0 and col < nc and grid[row][col] == 1: 
                                queue.append((row, col))
                                grid[row][col] = 0
                                count += 1
                    maxArea = max(maxArea, count)
        return maxArea
        



# @lc code=end

