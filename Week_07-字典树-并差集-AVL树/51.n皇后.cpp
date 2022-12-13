/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N皇后
 * theme 回溯
 */
#include<vector>
using namespace std;
// @lc code=start
class Solution {
private:
    vector<vector<string>> res;  //存结果
    vector<string> board;  //存棋盘
public:
    vector<vector<string>> solveNQueens(int n) {
        string line(n, '.');   //初始化一行
        backTrace(line, 0, n);  //从第0行开始
        return res;
    }
private:
    void backTrace(string& line, int row, int n) {
        //step1:回溯终止条件
        if (row >= n) {  //如果棋盘存够了n行，就不用再继续试下一行了
            res.push_back(board);
            return;
        }
        //step2:处理当前层逻辑
        for (int col=0; col<n; ++col) {  //在当前行，遍历每一列的元素，看是否可以放皇后
            if (checkAll(row, col, n)) {
                line[col] = 'Q';
                board.push_back(line);
                line[col] = '.';  //恢复为默认无皇后的空行，用于存下一行结果
        //step3:进入到下一层
                backTrace(line, row+1, n);
        //step4:恢复当前层状态
                board.pop_back(); //回溯处理返回的问题，如果return，那就把棋盘的上一行删掉；
            }
        }
    }
    bool checkAll(int row, int col, int n) {  //判断当前[row, col]位置是否适合放皇后？
        for(int i=1; i<=row; ++i) {
            if(col-i>=0 && board[row-i][col-i]=='Q') //左上
                return false;
            if(col+i<n && board[row-i][col+i]=='Q') //右上
                return false;
            if(board[row-i][col]=='Q') //上方
                return false;
        }
        return true;
    }
};
// @lc code=end

