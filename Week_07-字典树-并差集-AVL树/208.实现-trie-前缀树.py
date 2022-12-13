#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
# 字典树，参考官方答案
class Trie(object):

    def __init__(self):
        #子节点是代表26个字母的数组，某个元素不是None，那么代表这个子节点有效（有相应字母）
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            # 如果子节点不存在，就创建一个新的子节点
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
    def searchPrefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.searchPrefix(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

