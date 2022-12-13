#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        #方法1:递归
        ans = list()
        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
        '''
        #方法2:迭代
        ans = list()
        stack = list()
        while root or stack:
            while root:
                #处理根节点，连续向左
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return ans

# @lc code=end

