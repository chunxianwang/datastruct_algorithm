#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #把下面三条逻辑及其代码结合到一起思考：
        #递归终止条件：如果当前节点为空或p或q，返回当前节点
        #递归下探到下一层，遍历左子树，返回左子树是空，或是p或是q
        #递归下探到下一层，遍历右子树，返回右子树是空，或是p或是q
        if root==None or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        #如果左、有子树都不空，说明左右里面有p和q，root即公共祖先
        if left and right: return root
        #如果其中有一个子树不为空，则它里面有p或q，把它返回给上一层即可
        if left: return left
        else: return right

        
# @lc code=end

