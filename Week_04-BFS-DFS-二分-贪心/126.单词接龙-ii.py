#
# @lc app=leetcode.cn id=126 lang=python
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        result = list()
        if not wordList or endWord not in word_set:
            return result
        visited = {beginWord}
        length = len(beginWord)
        left = {beginWord}

        while left:
            next_level = set()
            for word in left:
                for j in range(length):
                    for m in range(26):
                        new_word = word[:j] + chr(ord('a')+m) + word[j+1:]
                        if new_word == endWord:
                            

# @lc code=end
