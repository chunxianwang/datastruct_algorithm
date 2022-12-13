/*
 * @lc app=leetcode.cn id=309 lang=cpp
 *
 * [309] 最佳买卖股票时机含冷冻期
 * tehme 动态规划
 */
/*
解题思路：
0.冷冻期概念定义：卖出股票后，你不能在第二天买入股票（即冷冻期为1天）
                即约束了买股票的条件，一定是前一天休息，大前天不持有股票
1. 状态定义
    dp[i][0]第i天不持有股票
    dp[i][1]第i天持有股票
2.状态转移:搞清楚当前状态由什么动作引起，做次动作之前是什么状态？如右式推倒：   当前状态 <== 相应动作（休息或买、卖股票） <==  之前状态
    不持有股票：
              今天休息，那就是昨天也没股票；
              今天卖股票，那就是昨天有股票；
         
    持有股票：
            今天休息，那就是昨天有股票
            今天买股票，那就是昨天休息，前天没股票
    
    昨天持有，今天休息；昨天不持有，今天买了
 */ 

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
#if 1
        int n = prices.size();
        if (n <= 1) return 0;
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = 0 - prices[0];
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1]);
        dp[1][1] = max(dp[0][1], 0 - prices[1]);
        for (int i = 2; i < n; i++) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]);
        }
        return max(dp[n-1][0], dp[n-1][1]);
#endif
#if 0
        int n = prices.size();
        if (n==0) return 0;
        int dp_i_0 = 0, dp_i_1 = -prices[0];
        int dp_pre_0 = 0;  //表示dp[i-2][0]
        for (auto price : prices) {
            int tmp = dp_i_0;
            dp_i_0 = max(dp_i_0, dp_i_1 + price);
            dp_i_1 = max(dp_i_1, dp_pre_0 - price);
            dp_pre_0 = tmp;  //更新滞后，用于表示dp[i-2][0]
        }
        return dp_i_0;
#endif
    }
};
// @lc code=end

