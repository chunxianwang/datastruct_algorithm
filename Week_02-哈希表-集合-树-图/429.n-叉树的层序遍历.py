#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        results = list()
        if not root:
            return results
        que = collections.deque([root])
        while que:
            result = list()
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.children:
                    que.extend(cur.children)  #注意，这里用extend逐个添加可迭代对象，而不是用append
            results.append(result)
        return results

        
# @lc code=end

