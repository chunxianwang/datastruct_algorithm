#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        关键在于题目要求时间复杂度为O(logN)
        显然从前往后的暴力搜索，时间复杂度O(N)不满足要求

        题解：二分查找，左右半边，有一个是升序的，在其中查看是否有target，如果没有，则在另外一边；
        反复执行上述二分查找过程
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target: return mid
            # 策略，左、右半边肯定有一个半边是有序的，那就在其中寻找target
            if nums[left] <= nums[mid]: # 左半边是有序的，就在左半边寻找target
                if nums[left] <= target < nums[mid]: #如果左半边有target，把搜索范围改为[left, mid-1]
                    right = mid - 1
                else: 
                    left = mid + 1
            else:                      # 右半边是有序的，就在右半边寻找target
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

