#
# @lc app=leetcode.cn id=713 lang=python
#
# [713] 乘积小于K的子数组
#

'''
使用一重循环枚举 right，同时设置 left 的初始值为 0。
在循环的每一步中，表示 right 向右移动了一位，将乘积乘以 nums[right]。
此时需要向右移动 left，直到满足乘积小于 k 的条件。
在每次移动时，需要将乘积除以 nums[left]。
当 left 移动完成后，对于当前的 right，就包含了 right−left+1 个乘积小于 k 的连续子数组。
'''

# @lc code=start
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# @lc code=end

