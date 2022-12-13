#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一：数组、倒序
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n):
            j = n-i-1
            if digits[j] != 9:
                digits[j] += 1
                return digits
            else:
                digits[j] = 0
        digits[0] = 1
        digits.append(0)
        return digits
# @lc code=end

