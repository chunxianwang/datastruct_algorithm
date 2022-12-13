#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#
'''
dp[][]状态是一个二维矩阵，列是word1，行是word2
dp[i][j]代表word1中的前i个字母转变为word2中的前j个字母的最小操作数
注意：动态规划转移方程是关注如何综合利用dp[i-1][j-1]、dp[i-1][j]和dp[i][j-1]，得到dp[i][j]
'''

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row = len(word1)
        col = len(word2)
        if row*col == 0: return row+col 
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1,row+1):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1,col+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        return dp[row][col]

# @lc code=end

