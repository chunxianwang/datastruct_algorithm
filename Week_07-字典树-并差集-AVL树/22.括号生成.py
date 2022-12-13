#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #回溯
        #定义lnum和rnum，分别是当前可添加左、右括号的数量
        def backtrack(ans, tmp, lnum, rnum):
            if lnum == 0 and rnum == 0:
                ans.append(tmp)
                return
            if rnum > 0:
                backtrack(ans, tmp+")", lnum, rnum-1)
            if lnum > 0:
                backtrack(ans, tmp+"(", lnum-1, rnum+1)
            
        ans = list()
        backtrack(ans, "", n, 0)
        return ans

# @lc code=end

