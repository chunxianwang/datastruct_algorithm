#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        #迭代+快速幂运算
        if n < 0: x, n = 1/x, -n
        ans = 1
        while n:
            if n & 1: ans *= x
            x *= x
            n >>= 1
        return ans
        '''
        #递归+快速幂运算
        def dfs(n):
            if n == 0:
                return 1.0
            y = dfs(n/2)
            if n % 2 == 0:
                return y*y
            else:
                return y*y*x
        if n < 0: x, n = 1/x, -n
        return dfs(n)

# @lc code=end

