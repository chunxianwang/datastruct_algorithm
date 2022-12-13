board = [
["E","E","E","E","E"],
["E","E","M","E","E"],
["E","E","E","E","E"],
["E","E","E","E","E"]]

click = [3, 0]



def updateBoard(board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    dic = [[-1, 0], [1, 0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]
    m = len(board)
    n = len(board[0])
    def search_around(x, y):
        count = 0
        for i, j in dic:
            x
            y
            if x+i >=0 and x+i < m and y+j >=0 and y+j < n:
                if board[x+i][y+j] == 'M':
                    count += 1
        return count
    def dfs(x, y):
        if x < 0 or x > m-1 or y < 0 or y > n-1:
            return
        if board[x][y] != 'E':
            return
        count = search_around(x, y)
        if count != 0:
            board[x][y] = str(count)
            return
        else:
            board[x][y] = 'B'
            for i, j in dic:
                dfs(x+i, y+j)
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board
    else:
        dfs(click[0], click[1])
        return board

updateBoard(board, click)
print(board)
