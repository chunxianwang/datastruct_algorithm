#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        #方法1
        #利用stack+迭代，实现中序遍历，如果不满足升序就返回False
        stack = list()
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
        '''
        #方法2
        #递归, 基于边界点递归法，
        #本质上是一个中序遍历，遍历过程中，得到判断是否搜索二叉树的结论
        #递归时，要特别注意，带入到下一层的内容（状态和待处理参数）
        #边界，就是下探到下一层时带入的当前层的状态（逻辑处理更新过的）
        def dfs(root, left, right):
            if root is None:
                return True
            if left < root.val < right:
                #//下探到左子树，就把根的值，作为上边界；下探到右子树，就把根的值，作为下边界
                return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            else:
                return False
        return dfs(root, -float('inf'), float('inf'))


# @lc code=end

