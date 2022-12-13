#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = nums[i] + dp[i-1][0]
        return max(dp[n-1][0], dp[n-1][1])
        

        
        #dp[i]，偷了n间房后，手里的钱
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[n]
        
        
        
# @lc code=end

