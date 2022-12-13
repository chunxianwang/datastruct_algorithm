#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m + n -1
        mi = m - 1
        ni = n - 1
        while mi >= 0 or ni >= 0:
            if mi == -1:
                nums1[i] = nums2[ni]
                ni -= 1
            elif ni == -1:
                nums1[i] = nums1[mi]
                mi -= 1
            elif nums1[mi] >= nums2[ni]:
                nums1[i] = nums1[mi]
                mi -= 1
            else:
                nums1[i] = nums2[ni]
                ni -= 1
            i -= 1
        return nums1


# @lc code=end
