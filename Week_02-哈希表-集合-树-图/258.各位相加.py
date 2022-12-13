#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        #方法1，O(1)复杂度
        if num!= 0 and num % 9 == 0:
            return 9
        else:
            return num % 9
        '''
        #方法2，暴力循环
        sum = 0
        while num >= 10:
            sum = 0
            while num != 0:
                sum += (num % 10)
                num = num / 10
            num = sum
        return num
# @lc code=end