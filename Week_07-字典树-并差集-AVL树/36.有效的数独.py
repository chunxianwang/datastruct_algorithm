#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        boxdict = defaultdict(set)
        n = len(board)
        m = 3
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val=='.':
                    continue
                if val in rowdict[i] or val in coldict[j] or val in boxdict[(i//m)*m+j//m]:
                    return False
                rowdict[i].add(val)
                coldict[j].add(val)
                boxdict[(i//m)*m+j//m].add(val)
        return True
# @lc code=end

