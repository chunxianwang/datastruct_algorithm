#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        #方法1:字典作为hashtable
        dictable = dict()
        for ch in s:
            if ch in dictable:
                dictable[ch] += 1
            else:
                dictable[ch] = 1
        for ch in t:
            if ch not in dictable:
                return False
            else:
                dictable[ch] -= 1
        for v in dictable.values():
            if v != 0:
                return False
        return True
        '''
        #方法2:用数组做hashtable
        table = [0] * 26
        for ch in s:
            a = ord('a')  #字符转ASCII码整数
            table[ord(ch)-a] += 1
        for ch in t:
            table[ord(ch)-a] -= 1
        for num in table:
            if num != 0:
                return False
        return True
# @lc code=end