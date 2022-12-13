#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
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
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        dfs(root)
        return ans
        '''
        #方法2:迭代
        ans = list()
        stack = list()
        prev = None
        while root or stack:
            #处理左节点，连续向左
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop() #弹出当前根节点
            #处理右节点
            if root.right and root.right != prev:  #如果右节点不空且没有被访问过，就把当前根节点再次入栈
                stack.append(root)
                root = root.right
            else:
                #处理根节点
                ans.append(root.val)
                #记录刚访问过的根节点
                prev = root
                root = None
            return ans

# @lc code=end

