#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n_nonezero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[n_nonezero] = nums[i]
                n_nonezero += 1
        for i in range(n_nonezero, n):
            nums[i] = 0

# @lc code=end

