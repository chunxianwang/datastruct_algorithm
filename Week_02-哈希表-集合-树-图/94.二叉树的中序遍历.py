#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        #方法1:递归
        #前序：根、左、右，即打印（输出）、左、右
        #中序：左、根、右，即左、打印（输出）、右
        #后序：左、右、根，即左、右、打印（输出）
        ans = list()
        #定义递归函数
        def dfs(root):
            #不满足条件返回上一层
            if not root:
                return
            #进入下一层
            dfs(root.left)
            #执行当前层动作，打印/输出
            ans.append(root.val)
            #进入下一层
            dfs(root.right)
        #进入递归函数
        dfs(root)
        #返回递归结果
        return ans
        """
        
        #方法2:非递归方法，迭代实现，使用栈（列表list）
        ''' 
        #代码风格1
        ans = list()
        stack = list()
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
			# 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
			# 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = tmp.right
        return ans
        '''
        #代码风格2
        ans = list()
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

# @lc code=end

