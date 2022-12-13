#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
# 简化问题描述：一棵二叉树，树上的每个点都有对应的权值，
#     每个点有两种状态（选中和不选中），问在不能同时选中有父子关系的点的情况下，
#     能选中的点的最大权值和是多少。
# 思路：利用深度搜索，以及保存每个节点选中和不选中时最大权值的字典
# 1. 当父节点被选中时，它的左右子节点都不能被选中，所以父节点的权值是父节点的值，加上左右子节点不被选中的权值
# 2. 当父节点不选中时，左右子节点都可以被选中或不选中，因此要对左右子节点求选中或不选中时权值的最大值，然后左右相加。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pick_map, self.nopick_map = {}, {}
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.dfs(node.right)
        # 注意，不一定有左、右子节点
        pick_left = self.pick_map[node.left] if node.left else 0
        pick_right = self.pick_map[node.right] if node.right else 0
        nopick_left = self.nopick_map[node.left] if node.left else 0
        nopick_right = self.nopick_map[node.right] if node.right else 0
        # 父节点值 加上左、右为选中的值
        pick = node.val + nopick_left + nopick_right
        # 左选中或不选中的最大值，加上右选中或不选中的最大值
        nopick = max(nopick_left, pick_left) + max(nopick_right, pick_right)
        self.pick_map.update({node : pick})
        self.nopick_map.update({node : nopick})

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return max(self.nopick_map[root], self.pick_map[root])

# @lc code=end

