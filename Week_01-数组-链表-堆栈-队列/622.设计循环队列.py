#
# @lc app=leetcode.cn id=622 lang=python
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue(object):

# 数组
# 通过一个数组进行模拟，通过操作数组的索引构建一个虚拟的首尾相连的环。在循环队列结构中，
# 设置一个队尾 rear 与队首 front，且大小固定的数组。
# 在循环队列中，当队列为空，可知 front=rear；而当所有队列空间全占满时，也有 front=rear。
# 为了区别这两种情况，假设队列使用的数组有 capacity 个存储空间，则此时规定循环队列最多只能有capacity−1 个队列元素，
# 当循环队列中只剩下一个空存储单元时，则表示队列已满。根据以上可知，队列判空的条件是 front=rear，
# 而队列判满的条件是 front=(rear+1)modcapacity。
# 注意：front是指向有效队列头第一个元素上，rear是指向有效队列尾之后的一个元素上
    def __init__(self, k):
        """
        :type k: int
        """
        self.front = self.rear = 0
        self.elements = [0]*(k+1)


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear+1) % len(self.elements)
        return True


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front+1) % len(self.elements)
        return True


    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.elements[self.front]



    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.elements[(self.rear-1)%len(self.elements)]


    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.rear == self.front


    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % len(self.elements) == self.front



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

