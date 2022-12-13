#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        '''
        #递归法
        ans = list()
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            ans.append(root.val)
        dfs(root)
        return ans
        '''
        #迭代法

        
# @lc code=end

