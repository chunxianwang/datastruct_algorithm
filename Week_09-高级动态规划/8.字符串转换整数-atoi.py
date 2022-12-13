#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#
# 练习写确定有限状态机，详细题解内容见leetcode官方题解
# 类似题目：393. UTF-8 编码验证【中等】
#         65. 有效数字【困难】
# @lc code=start
INT_MAX = 2**31-1
INT_MIN = -2**31
class Automation:
    def __init__(self):
        # 定义初始状态
        self.state = 'start'
        # 初始化符号
        self.sign = 1
        # 初始化数值
        self.ans = 0
        # 定义状态机的状态转换表
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
    # 获取状态转换过程条件
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3
    # 根据状态更新数值和符号
    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans*10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)

        if self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 初始化自动状态机
        automation = Automation()
        for c in s:
            automation.get(c)
        return automation.sign * automation.ans
# @lc code=end

