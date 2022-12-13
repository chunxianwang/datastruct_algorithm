#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
from collections import defaultdict
    
class Solution(object):
    '''
    # 此方法超时!!!
    directs = [(1, 0), (-1, 0), (0, 1), (0,-1)]
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = list()
        m = len(board)
        if m == 0: return ans
        n = len(board[0])
        for word in words:
            mark = [[0 for _ in range(n)] for _ in range(m)]
            inboard = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        #把该元素记为已使用
                        mark[i][j] = 1
                        if self.backtrack(i, j, mark, board, word[1:]) == True:
                            inboard = True
                        else:#回溯
                            mark[i][j] = 0
            if inboard: ans.append(word)
        return ans

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False
    '''

    # 针对上面dfs回溯超时：
    # 采用统计单词字母个数加速，比如某个单词要10个'e'，棋盘上一共9个'e'，那必然不能构成这个单词
    directs = [(1, 0), (-1, 0), (0, 1), (0,-1)]
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = list()
        m = len(board)
        if m == 0: return ans
        n = len(board[0])
        #统计board中各元素数目
        dic_board = defaultdict(int)
        for i in range(m):
            for j in range(n):
                dic_board[board[i][j]] += 1
        
        for word in words:
            mark = [[0 for _ in range(n)] for _ in range(m)]
            dic_word = defaultdict(int)
            #统计word中各元素数目，并判断是否大于board中相应元素
            exceedboard = False
            for s in word:
                dic_word[s] += 1
            for k, v in dic_word.items():
                if v > dic_board[k]: 
                    exceedboard = True
                    break
            if exceedboard:
                continue

            inboard = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        #把该元素记为已使用
                        mark[i][j] = 1
                        if self.backtrack(i, j, mark, board, word[1:]) == True:
                            inboard = True
                        else:#回溯
                            mark[i][j] = 0
            if inboard: ans.append(word)
        return ans
    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False

# @lc code=end

