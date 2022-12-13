#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成: 可以抽象成一个部分裁剪的二叉树，添加左括号就是左子树
# 添加右括号就是右子树。有些右子树（右括号比左括号多）要被裁剪掉。
# 可以按照二叉树深度优先搜索来组织算法代码
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = list()
        #回溯
        #定义lnum和rnum，分别是当前可添加左、右括号的数量
        def backtrack(tmp, lnum, rnum):
            if lnum == 0 and rnum == 0:
                ans.append(tmp)
                return
            if rnum > 0:
                backtrack(tmp+")", lnum, rnum-1)
            if lnum > 0:
                backtrack(tmp+"(", lnum-1, rnum+1)
        
        backtrack("", n, 0)
        return ans

# @lc code=end

