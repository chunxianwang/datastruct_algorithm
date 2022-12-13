#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存机制
#

# LRU 缓存机制可以通过哈希表辅以双向链表实现，我们用一个哈希表和一个双向链表维护所有在缓存中的键值对。
# 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
# 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
# 这样以来，我们首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，即可在 
# O(1) 的时间内完成 get 或者 put 操作。具体的方法如下：
# 对于 get 操作，首先判断 key 是否存在：
#   如果 key 不存在，则返回 −1；
#   如果 key 存在，则 key 对应的节点是最近被使用的节点。通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。
# 对于 put 操作，首先判断 key 是否存在：
#   如果 key 不存在，使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，并将 key 和该节点添加进哈希表中。然后判断双向链表的节点数是否超出容量，如果超出容量，则删除双向链表的尾部节点，并删除哈希表中对应的项；
#   如果 key 存在，则与 get 操作类似，先通过哈希表定位，再将对应的节点的值更新为 value，并将该节点移到双向链表的头部。
# 上述各项操作中，访问哈希表的时间复杂度为 O(1)，在双向链表的头部添加节点、在双向链表的尾部删除节点的复杂度也为 O(1)。
# 而将一个节点移到双向链表的头部，可以分成「删除该节点」和「在双向链表的头部添加节点」两步操作，都可以在 O(1) 时间内完成。
# 小技巧：在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限，这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在。

# @lc code=start
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value  = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        # 如果key存在，县通过哈希表定位它的node，再移到头部，并返回node的value
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            # 如果key 不存在，创建一个新的key:value节点
            node = DLinkedNode(key, value)
            # 新节点添加进哈希表。哈希表中存的是key: node
            self.cache[key] = node
            # 添加到双向链表头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表尾部节点
                removed = self.removeTail()
                # 相应地删除哈希表中对应的key项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果key存在，先通过哈希表定位它的node，再修改value，再移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    # 双向链表基础操作--添加头
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    # 双向链表基础操作--删除节点
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    # 双向链表基础操作--把节点移动到头
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    # 双向链表基础操作--删除尾节点
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

