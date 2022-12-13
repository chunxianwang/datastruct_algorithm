#
# @lc app=leetcode.cn id=1021 lang=python
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        思路二：参考最佳题解，
        初始化，跳过最外面的左括号，左括号计数初始为1，右为0
        枚举字符串中的字符对左右括号进行计数；
            如果左右计数不相等，把当前字符放入结果字符串ans；
            否则，不放入结果字符串，重新执行“初始化”过程，继续枚举字符；
        枚举结束，返回ans。
        '''
        L = 1
        R = 0
        ans = ""
        i = 1
        while i < len(s):
            if s[i] == "(": L += 1
            else: R += 1
            if (R != L): ans += s[i]
            else:
                i += 1
                L = 1
                R = 0
            i += 1
        return ans

# @lc code=end

