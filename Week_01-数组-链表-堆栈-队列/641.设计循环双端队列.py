#
# @lc app=leetcode.cn id=641 lang=python
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque(object):

# 数组方法
# 注意：front是指向有效队列头第一个元素上，rear是指向有效队列尾之后的一个元素上
    def __init__(self, k):
        """
        :type k: int
        """
        self.front = self.rear = 0
        self.elements = [0] * (k+1)


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front-1) % len(self.elements)
        self.elements[self.front] = value
        return True


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear+1) % len(self.elements)
        return True


    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front+1) % len(self.elements)
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear-1) % len(self.elements)
        return True


    def getFront(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.elements[self.front]


    def getRear(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.elements[(self.rear-1)%len(self.elements)]



    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == self.rear


    def isFull(self):
        """
        :rtype: bool
        """
        return self.front == (self.rear+1) % len(self.elements)



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

