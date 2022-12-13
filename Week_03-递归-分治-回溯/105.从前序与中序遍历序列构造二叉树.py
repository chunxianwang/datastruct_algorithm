#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (preorder and inorder):
            return None
        # 根据前序数组的第一个元素，就可以确定根节点
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素
        mid_index = inorder.index(preorder[0])
        # 递归的处理前序数组的左边部分和中序数组的左边部分
        root.left = self.buildTree(preorder[1:mid_index+1], inorder[:mid_index])
        # 递归处理前序数组右边部分和中序数组右边部分
        root.right = self.buildTree(preorder[mid_index+1:],inorder[mid_index+1:])
        return root

# @lc code=end

