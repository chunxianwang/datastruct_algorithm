#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1: return 0
        dp = [0] * n
        ans = 0
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2+(dp[i-2] if i>1 else 0)
                else:
                    if i-dp[i-1] > 0 and s[i-dp[i-1]-1]=='(':
                        dp[i] = dp[i-1]+2+(dp[i-dp[i-1]-2] if i-dp[i-1]>1 else 0)
                ans = max(ans, dp[i])
        return ans
                    
# @lc code=end

