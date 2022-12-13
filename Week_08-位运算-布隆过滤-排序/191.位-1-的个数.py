#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hwweight = 0
        for i in range(32):
            hwweight += (n&1)
            n >>= 1
        return hwweight
        
# @lc code=end

