#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#等效性地理解题目要求：和边界'O'连通的'O‘保留，其余所有元素都置为’X‘

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(board, r, c):
            if r>=0 and c>=0 and r<len(board) and c<len(board[0]) and board[r][c]=='O':
                board[r][c]='1'
                dfs(board, r-1, c)
                dfs(board, r+1, c)
                dfs(board, r, c-1)
                dfs(board, r, c+1)
                
        if len(board) == 0: return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            dfs(board, i, 0)
            dfs(board, i, col-1)
        for j in range(col):
            dfs(board, 0, j)
            dfs(board, row-1, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
# @lc code=end

