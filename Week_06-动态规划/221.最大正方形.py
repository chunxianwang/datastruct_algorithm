#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0: return 0
        col = len(matrix[0])
        dp = [[0]*(col)]*(row)
        dp = [[0] * col for _ in range(row)]
        Max = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i==0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                Max = max(Max, dp[i][j])
        return Max * Max


# @lc code=end

