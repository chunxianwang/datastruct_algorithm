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
        board = list()  #存棋盘
        ans = list()  #存结果
        line = [0] * n  #代表每一行
        #检查是否重合
        def checkAll(row, col, n):
            for i in range(1,row+1):
                if col - i >=0 and board[row-i][col-i] == 'Q':
                    return False
                if col +i < n and board[row-i][col+i] == 'Q':
                    return False
                if board[row-i][col] == 'Q':
                    return False
            return True
        #递归，把处理某一行作为当前层
        def dfs(line, row):
            #如果棋盘满了，就放入结果并退回
            if len(board) == n:
                ans.append(board[:])
                return
            #在当前行尝试在各列放入Q
            for i in range(n):
                if checkAll(row, i, n):
                    line[i] = 1
                    str = ""
                    for j in range(n):
                        if line[j]==0: str += '.'
                        else: str+= 'Q'
                    board.append(str)
                    line[i] = 0
                    dfs(line, row+1)
                    board.pop()
        dfs(line, 0)
        return ans
# @lc code=end

