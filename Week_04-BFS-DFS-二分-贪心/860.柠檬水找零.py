#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5: 
                five += 1
                continue
            if bill == 10 and five>0: 
                five -= 1
                ten += 1
                continue
            if bill == 20:
                if ten>0 and five>0: 
                    five -= 1
                    ten -= 1
                    continue
                else:
                    if five>2:
                        five -= 3
                        continue
            return False
        return True

# @lc code=end

