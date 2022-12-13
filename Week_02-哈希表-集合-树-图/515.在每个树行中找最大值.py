#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = list()
        if root is None: return ans
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            Max = float('-inf')
            for i in range(size):
                cur = queue.popleft()
                Max = max(Max, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(Max)
        return ans

# @lc code=end

