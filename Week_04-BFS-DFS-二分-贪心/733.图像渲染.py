#
# @lc app=leetcode.cn id=733 lang=python
#
# [733] 图像渲染
#

# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        '''
        # 深度优先搜索
        nr = len(image)
        nc = len(image[0])
        directions = {(-1, 0), (1, 0), (0,-1), (0,1)}
        sColor = image[sr][sc]
        def dfs(row, col):
            if row >= nr or col >= nc or row < 0 or col < 0 or image[row][col] != sColor or image[row][col] == newColor:
                return
            image[row][col] = newColor
            for direction in directions:
                dfs(row+direction[i][0], col+direction[i][1])
        dfs(sr, sc)
        return image
        '''

        # 广度优先搜索
        sColor = image[sr][sc]
        sColor = image[sr][sc]
        if sColor == newColor:
            return image
        nr = len(image)
        nc = len(image[0])
        directions = {(-1, 0), (1, 0), (0,-1), (0,1)}
        queue = collections.deque()
        queue.append((sr, sc))
        while queue:
            point = queue.popleft()
            image[point[0]][point[1]] = newColor
            for direction in directions:
                row = point[0] + direction[0]
                col = point[1] + direction[1]
                if row >= 0 and row < nr and col >= 0 and col < nc and image[row][col] == sColor:
                    queue.append((row, col))
        return image
        
# @lc code=end

