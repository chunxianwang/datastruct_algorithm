#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = list()
        if root is None: return root
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            sum = 0
            for _ in range(size):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(float(sum)/size)
        return ans        
# @lc code=end

