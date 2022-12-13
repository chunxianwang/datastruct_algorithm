#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号：字典、栈
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        #用dict
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs: #当前是右括号，即判断临近元素是否对应左括号
                #list[-1]，表示列表中最后一个元素
                # if not list，判断列表为空，即空列表是True
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else: #当前是左括号，即入栈
                stack.append(ch)
        return not stack  #列表空即为True，列表非空即为False
# @lc code=end

