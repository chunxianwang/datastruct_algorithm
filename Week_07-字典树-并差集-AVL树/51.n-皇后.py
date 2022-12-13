#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = list()
        ans = list()
        line = [0] * n #代替某一列的列表，用列表来表示，便于用line[i]的方式查询
        def checkAll(row, col):
            for i in range(1, row+1):
                if col-i >= 0 and board[row-i][col-i] == 'Q': #check左上
                    return False
                if col+i < n and board[row-i][col+i] == 'Q': #check右上
                    return False
                if board[row-i][col] == 'Q': #check上方
                    return False
            return True
        def dfs(row):
            #如果棋盘满了，就放入结果并返回
            if len(board) == n:
                ans.append(board[:])
                return
            # 在当前行尝试在各列放入Q
            for i in range(n):
                if checkAll(row, i):
                    line[i] = 1
                    str = ''
                    for j in range(n): str += '.' if line[j]==0 else 'Q'
                    board.append(str)
                    line[i] = 0
                    # 进入下一层
                    dfs(row+1)
                    # 恢复状态
                    board.pop()
        dfs(0)
        return ans
# @lc code=end

