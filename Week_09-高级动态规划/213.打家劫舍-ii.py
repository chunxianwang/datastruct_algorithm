#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
# 相比于首位两家不是环形，这里分两种情况：
# 偷第一家，不偷最后一家；不偷第一家，偷最后一家
# 按照计算198题计算这两种情况，然后求最大一个就行

# @lc code=start
class Solution(object):
    def robrange(self, nums, start, end):
        if start > end:
            return 0
        n = end - start
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[start]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[start+i]
        return max(dp[n-1][0], dp[n-1][1])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        rob_first_nolast = self.robrange(nums, 0, n-1)
        rob_nofirst_last = self.robrange(nums, 1, n)
        return max(rob_first_nolast, rob_nofirst_last)


    
# @lc code=end

