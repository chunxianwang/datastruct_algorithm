#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
'''
1.dp问题，公式为：dp[i] = max(nums[i], nums[i]+dp[i-1]);
2.最大子序列和 = 当前元素自身最大，或包含之前后最大；
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float("-inf")] * n#定义状态数组
        dp[0] = nums[0] #定义状态base
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+ nums[i], nums[i]) #状态转移
            ans = max(ans, dp[i])
        return ans
# @lc code=end

