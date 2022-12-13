#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        #方法1:递归调用函数本身
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        '''
        #方法2:新写一个递归函数
        def dfs(root):
            if root:
                root.left, root.right = root.right, root.left
                dfs(root.left)
                dfs(root.right)
            else:
                return
        dfs(root)
        return root
        
# @lc code=end

