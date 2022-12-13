#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#
'''
自底向上，动态规划：
当前位置路径，为下一层相邻两个元素路径较小者+当前位置路径的大小
'''

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [t for t in triangle[n-1]]
        i = n-2
        while i >= 0:
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
            i -= 1
        return dp[0]


# @lc code=end

