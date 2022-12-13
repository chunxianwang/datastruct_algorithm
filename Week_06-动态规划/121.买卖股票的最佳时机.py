#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
'''
定义状态dp[i][j]是第i天手里的现金数目
dp[i][0]：第i天，不持有股票时，手里的现金
dp[i][1]：第i天，持有股票时，手里的现金

#注意和122的差别在于，此题目中不能多次买卖股票，因此当前持有股票的话，一种是原来持有股票当前继续持有
另外一种是，原来没买过，今天买下股票:0-prices[i]
不可能的情况是多次买卖：dp[i][0]-prices[i]


'''


# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0]*2]*(n)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])  
        return dp[n-1][0]



# @lc code=end

