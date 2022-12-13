#
# @lc app=leetcode.cn id=552 lang=python
#
# [552] 学生出勤记录 II
#
# 题解：动态规划方法
# 可奖励的出勤记录要求：同时满足缺勤次数少于2 和连续迟到次数少于 3，因此动态规划的状态由总天数、缺勤次数和结尾连续迟到次数决定。
# （由于不会记录连续迟到次数等于或多于 3 的情况，因此非结尾的连续迟到次数一定少于 3，只需要记录结尾连续迟到次数即可）。
# 定义 dp[i][j][k] 表示前 i 天有 j 个 ‘A’ 且结尾有连续 k 个 ‘L’ 的可奖励的出勤记录的数量，其中 0≤i≤n，0≤j≤1，0≤k≤2。
# 当 i=0 时，没有任何出勤记录，此时 ‘A’ 的数量和结尾连续 ‘L’ 的数量一定是 0，因此动态规划的边界情况是 dp[0][0][0]=1。
# 当 1≤i≤n 时，dp[i][][] 的值从 dp[i−1][][] 的值转移得到，计算每个状态的值，需要考虑第 i 天出勤记录的3种情况（‘P’、‘A’和‘L’）

# @lc code=start
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            # 如果第i天是‘P’， 第i天可以是0或1个‘A’，且是0个连续‘L’结尾。相应地：第i-1天可以是0或1个‘A’，以及0、1、2个连续‘L’结尾；
            for j in range(0,2):
                for k in range(0,3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
            
            # 如果第i天是‘L’，第i天可以是0或1个‘A’，以及可以1个或2个连续‘L’结尾。相应地：第i-1天是0或1个‘A’，以及0个或1个连续'L'结尾；
            for j in range(0,2):
                for k in range(1,3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
            
            # 如果第i天是'A'，第i天是1个‘A’，以及0个‘L’结尾。相应地：第i-1天是0个‘A’，以及0、1或2个‘L’结尾：
            for k in range(0,3):
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD
        
        total = 0
        for j in range(0,2):
            for k in range(0,3):
                total += dp[n][j][k]
        return total % MOD

# @lc code=end

