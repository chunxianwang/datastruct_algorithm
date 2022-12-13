#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1, h2 = l1, l2
        tmp = 0
        while h1 or h2: # 需要遍历最长的数
            val = h1.val + h2.val + tmp # 值=l1 + l2 +进位
            h1.val, tmp = val%10, val//10
            if not h1.next and h2.next: h1.next = ListNode(0) # 如果l1太短，添节点0
            if not h2.next and h1.next: h2.next = ListNode(0) # 如果l2太短，添节点0
            if not h1.next and not h2.next:  # 如果两个一样短，判断是否有进位，有就添节点
                if tmp: h1.next = ListNode(tmp)
                return l1 # 两个一样短的时候必然是返回的时候
            h1 = h1.next
            h2 = h2.next
        
# @lc code=end

