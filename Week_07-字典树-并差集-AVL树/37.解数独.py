#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set(range(1,10)) for _ in range(9)] #行剩余可用数字
        col = [set(range(1,10)) for _ in range(9)] #列剩余可用数字
        box = [set(range(1,10)) for _ in range(9)] #块剩余可用数字
        empty = [] #收集需要填充的位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  #更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[(i//3)*3+j//3].remove(val)
                else:
                    empty.append((i,j))  #统计要填充的位置
        def backtrack(iter):
            if iter == len(empty):  #处理完要填充的位置就找到了答案
                return True
            i, j = empty[iter]
            for val in row[i] & col[j] & box[(i//3)*3+j//3]:
                row[i].remove(val)
                col[j].remove(val)
                box[(i//3)*3+j//3].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1): return True  
                row[i].add(val)
                col[j].add(val)
                box[(i//3)*3+j//3].add(val)
            return False
        backtrack(0)
        


# @lc code=end

