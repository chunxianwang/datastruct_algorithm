#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return max(dp[n-1][1], dp[n-1][0])

# @lc code=end

