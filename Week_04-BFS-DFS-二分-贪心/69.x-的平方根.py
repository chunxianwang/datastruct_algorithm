#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #二分查找： x平方根的整数部分k是满足 k^2 <= k 的最大k值
        # 
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans

# @lc code=end

