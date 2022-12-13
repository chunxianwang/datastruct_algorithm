#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        num = 0
        j = 0
        for i in range(len(g)):
            while j < len(s):
                if g[i] <= s[j]:
                    j += 1
                    num += 1
                    break
                j += 1
        return num
# @lc code=end

