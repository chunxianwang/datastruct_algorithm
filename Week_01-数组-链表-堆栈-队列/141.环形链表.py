#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表：链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #两种方法：快慢指针-龟兔赛跑，字典中查询是否有重复的节点
        #        字典查询
        '''
        
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        '''
        dictable = dict()
        prev = head
        while prev:
            if prev in dictable:
                return True
            else:
                dictable[prev] = 1
            prev = prev.next
        return False
        
# @lc code=end

