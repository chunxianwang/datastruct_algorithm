#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #数组放入字典再查询，注意字典内要对元素计数
        n1 = len(nums1)
        n2 = len(nums2)
        dictable1 = dict()
        ans = list()
        for i in range(n1):
            if nums1[i] in dictable1:
                dictable1[nums1[i]] += 1
            else:
                dictable1[nums1[i]] = 1
        for j in range(n2):
            if nums2[j] in dictable1 and dictable1[nums2[j]] > 0:
                ans.append(nums2[j])
                dictable1[nums2[j]] -= 1
        return ans


# @lc code=end

