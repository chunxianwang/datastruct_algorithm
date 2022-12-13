#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if not wordList or endWord not in word_set:
            return 0
        visited = {beginWord, endWord}
        left, right = {beginWord}, {endWord}
        number = 0
        length = len(beginWord)
        while left:
            number += 1
            next_level = set()
            for word in left:
                for j in range(length):
                    for m in range(26):
                        new_word = word[:j] + chr(ord('a')+m) + word[j+1:]
                        if new_word in right:
                            return number+1
                        if new_word not in visited and new_word in word_set:
                            visited.add(new_word)
                            next_level.add(new_word)
            left = next_level
            if len(left) > len(right):
                left, right = right, left
        return 0
# @lc code=end

