#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = list()
        if not root:
            return results
        queue = collections.deque([root])
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
            results.append(result)
        
        ans = list()
        while results:
            ans.append(results.pop())
        return ans
# @lc code=end

