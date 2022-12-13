#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#
# 倒序遍历字符串

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = len(s) - 1
        while s[index] == ' ':
            index -= 1
        Len = 0
        while index >= 0 and s[index] != ' ':
            Len += 1
            index -= 1
        return Len
# @lc code=end

