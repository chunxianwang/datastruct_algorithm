#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())

        L= 0
        R = len(sgood) - 1
        
        while L < R:
            if sgood[L] != sgood[R]:
                return False
            L += 1
            R -= 1
        return True
# @lc code=end

