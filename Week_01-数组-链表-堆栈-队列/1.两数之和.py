#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()               #创建空字典 也可以用 hashtable = {}
        for i, num in enumerate(nums):   #枚举列表元素的方法
            if target - num in hashtable:
                return[hashtable[target-num], i]
            hashtable[num] = i
        return []
# @lc code=end

