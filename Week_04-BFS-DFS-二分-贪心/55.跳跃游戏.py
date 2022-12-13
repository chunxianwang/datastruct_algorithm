#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        for i in range(len(nums)):
            if i > maxpos:
                return False
            maxpos = max(i+nums[i], maxpos)
        return True

# @lc code=end

