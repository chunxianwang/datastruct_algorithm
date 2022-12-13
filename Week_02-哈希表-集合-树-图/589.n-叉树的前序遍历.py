#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root):
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
            ans.append(root.val)
            for child in root.children: #遍历各子节点
                dfs(child)
        dfs(root)
        return ans
        '''
        #迭代法
        ans = list()
        stack = list()
        if not root:
            return ans
        stack.append(root)
        while stack:
            root = stack.pop()
            ans.append(root.val)
            stack.extend(root.children[::-1])  #children[::-1]可以倒序列举所有的child，最后一个加入的最左边的child，这样先弹出的也是左孩子
        return ans
        
        
# @lc code=end

