#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        leftindex = 0
        rightindex = n-1
        maxvolum = 0
        while leftindex < rightindex:
            maxvolum = max(maxvolum, (rightindex-leftindex) * min(height[leftindex], height[rightindex]))
            if height[leftindex] < height[rightindex]:
                leftindex += 1
            else:
                rightindex -= 1
        return maxvolum

# @lc code=end

