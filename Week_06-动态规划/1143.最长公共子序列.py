#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start

#第一步，定义dp状态；
#       对于两个字符串的动态规划问题，都可以定义以两个字符串为边的
#       二维数组dp[s1.size()][s2.size()]，这里数组中的元素dp[i][j]表示，
#       对于s1[1,2,...i]和s2[1,2,...j]，他们的lcs长度是dp[i][j];
#第二步，定义base case，
#       定义第一行和第一列，这样可以很好支持第二行、列进行状态转移，（要用到第一行、列的状态）；
#第三部，定义状态转移方程
#       这是最难的一步，
#       如果s1[i]==s2[j];dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
#       如果s1[i]!=s2[j];dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1];
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 在dp table中增加了一行‘’ 和一列‘’，表示空字符串，这样容易实施第二部 定义base case
        row = len(text1)
        col = len(text2)
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[row][col]
# @lc code=end

