#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项：数组
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #注意，要求原地操作，返回数组/列表长度
        if len(nums) == 0: return 0
        index = 0   #不重复元素指针
        for num in nums:
            if num != nums[index]:
                index += 1
                nums[index] = num
        return index+1
# @lc code=end

