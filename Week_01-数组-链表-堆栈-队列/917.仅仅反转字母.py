#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 仅仅反转字母
#

# @lc code=start

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = list(s)  #把string初始化成字符数组
        left = 0
        right = n -1
        while left < right:
            while left < right and not ans[left].isalpha():
                left += 1
            while left < right and not ans[right].isalpha():
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)#把数组中的字符合并成string
        
# @lc code=end

