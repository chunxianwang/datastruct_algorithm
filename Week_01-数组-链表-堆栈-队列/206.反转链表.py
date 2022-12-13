#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表：链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #核心是改变链表中每个节点的指向
        pre = None
        cur = head
        while cur:
            #暂存原链表的下一节点
            tmp = cur.next
            #原链表当前节点指向改变：指向了前面
            cur.next = pre
            #走向下一个节点
            pre = cur
            cur = tmp
        return pre
# @lc code=end

