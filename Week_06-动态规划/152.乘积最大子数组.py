#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dpmin = [float("inf")]*n
        dpmax = [float("-inf")]*n
        dpmin[0] = nums[0]
        dpmax[0] = nums[0]
        ans = dpmax[0]
        for i in range(1, n):
            dpmin[i] = min(dpmin[i-1]*nums[i], dpmax[i-1]*nums[i], nums[i])
            dpmax[i] = max(dpmin[i-1]*nums[i], dpmax[i-1]*nums[i], nums[i])
            ans = max(ans, dpmax[i])
        return ans

# @lc code=end

