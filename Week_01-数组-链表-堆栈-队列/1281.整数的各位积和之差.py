#
# @lc app=leetcode.cn id=1281 lang=python
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        add = 0
        mul = 1
        while n > 0:
            digit = n%10
            n //= 10
            add += digit
            mul *= digit
        return mul - add

# @lc code=end

