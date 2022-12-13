#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 轮转数组
#

# @lc code=start
class Solution(object):
    def reverse(self, nums, begin, end):
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


# @lc code=end

