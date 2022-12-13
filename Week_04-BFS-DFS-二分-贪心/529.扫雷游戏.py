#
# @lc app=leetcode.cn id=529 lang=python
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        dic = [[-1, 0], [1, 0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]
        
        def search_around(x, y): #看看周围有几个雷
            count = 0
            for i, j in dic:
                if x+i >=0 and x+i < m and y+j >=0 and y+j < n:
                    if board[x+i][y+j] == 'M':
                        count += 1
            return count
        def dfs(x, y):  #深度优先搜索
            if x < 0 or x > m-1 or y < 0 or y > n-1: #先判断是不是超出边界
                return
            if board[x][y] != 'E':  #再判断是不是空
                return
            count = search_around(x, y) #算一下有多少雷
            if count != 0:   #有雷就截断，不再继续递归寻找了
                board[x][y] = str(count)
                return
            else:
                board[x][y] = 'B'
                for i, j in dic:
                    dfs(x+i, y+j)
        m = len(board)
        n = len(board[0])
        if board[click[0]][click[1]] == 'M':  #可能一开始就踩雷
            board[click[0]][click[1]] = 'X'
            return board
        else:
            dfs(click[0], click[1])
            return board
# @lc code=end

