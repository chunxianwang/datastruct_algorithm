#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #相比于102题目，只增加了处理逆序遍历的过程
        results = list()
        if root is None: return results
        queue = collections.deque([root])
        reverse = False
        while queue:
            size = len(queue)
            result = list()
            for _ in range(size):
                cur = queue.popleft()
                result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if reverse:
                results.append(result[::-1])
            else:
                results.append(result)
            reverse = not reverse
        return results


# @lc code=end

