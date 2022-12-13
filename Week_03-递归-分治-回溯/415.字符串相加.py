#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        #方法1：手动实现逐位相加，注意string中各位的方向
        ln1 = len(num1) - 1
        ln2 = len(num2) - 1
        carry = 0
        tmp = ""
        ans = ""
        while (ln1>=0 or ln2>=0 or carry):
            if ln1<0:
                x = 0
            else:
                x = int(num1[ln1])
                ln1 -= 1
            if ln2<0:
                y = 0
            else:
                y = int(num2[ln2])
                ln2 -= 1
            tmp += str(((x+y+carry)% 10))
            carry = (x+y+carry)/10
        n = len(tmp) - 1
        while n >= 0:
            ans += tmp[n]
            n -= 1
        return ans
        '''
        #方法2:str转数字再转回str
        a = int(num1)
        b = int(num2)
        c = a+b
        return str(c)

        
# @lc code=end

