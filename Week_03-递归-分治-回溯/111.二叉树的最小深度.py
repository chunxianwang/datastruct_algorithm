#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        递归法：
        针对当前层，存在3种情况：
        1.当前root为空，那么跳出递归，且返回深度值0；
        2.当前root左或右子树为空，那么也可以结束递归，
            返回不为空的子树深度+1（操作技巧，其中一个是0，那么可以把两者相加再+1）
        3.当前root的左、右子树都不是空，那么返回左右子树的较小深度+1
        '''
        if root == None: return 0
        depth1 = self.minDepth(root.left)
        depth2 = self.minDepth(root.right)
        if (root.left == None or root.right == None):
            #depth1和depth3中，有一个是0
            return depth1 + depth2 + 1
        else:
            return min(depth1, depth2) + 1
# @lc code=end

