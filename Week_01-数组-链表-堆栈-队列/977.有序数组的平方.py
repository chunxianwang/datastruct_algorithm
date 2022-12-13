#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
# step1, 找到负数和非负数的分界点
# step2，从分界点向两端遍历，分三种情况：已遍历完了负数，已遍历完了正数，两者都没遍历完
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        neg_index = -1
        for i, num in enumerate(nums):
            if num < 0:
                neg_index = i
            else:
                break
        ans = list()
        i, j = neg_index, neg_index+1
        while i>=0 or j<n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i]* nums[i])
                i -= 1
            elif nums[i]* nums[i] < nums[j]*nums[j]:
                ans.append(nums[i]*nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
        return ans

# @lc code=end

