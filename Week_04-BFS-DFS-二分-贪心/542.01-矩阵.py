#
# @lc app=leetcode.cn id=542 lang=python
#
# [542] 01 矩阵
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        
        return dist
# @lc code=end

