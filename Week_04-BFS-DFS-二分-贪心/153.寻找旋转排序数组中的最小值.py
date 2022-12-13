#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  #注意这里不是right = mid - 1
        return nums[left]
# @lc code=end

