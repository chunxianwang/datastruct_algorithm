#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
# 状态：从数组首部到第i元素的最长上升子序列的长度dp[i]
# 状态转移方程：
# 遍历所有的i，求出以各个元素为终点的最长上升子序列，然后比较所有的dp[i]，求出最大值，即整个数组的最长上升子序列长度；

# 如何求dp[i]呢？
# 遍历0～i-1的数组元素，如果某个元素num[j]小于nums[i]，则dp[i] = max (dp[i], dp[j] + 1);
# 即等于以j为终点的最长上升子序列长度+1，或 dp[i]的较大值。

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

