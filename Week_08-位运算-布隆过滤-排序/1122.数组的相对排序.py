#
# @lc app=leetcode.cn id=1122 lang=python
#
# [1122] 数组的相对排序
# 思路： 计数排序

# @lc code=start
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        upper = max(arr1)
        frequency = [0]*(upper+1)
        for x in arr1:
            frequency[x] += 1
        ans = list()
        for x in arr2:
            ans.extend([x]*frequency[x])
            frequency[x] = 0
        for x in range(upper+1):
            if frequency[x] > 0:
                ans.extend([x]*frequency[x])
        return ans
# @lc code=end

