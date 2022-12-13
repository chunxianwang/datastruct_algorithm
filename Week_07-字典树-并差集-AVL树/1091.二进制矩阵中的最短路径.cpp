/*
 * @lc app=leetcode.cn id=1091 lang=cpp
 *
 * [1091] 二进制矩阵中的最短路径
 * theme 高级搜索
 * theme bfs
 * theme 启发式搜索
 */

// @lc code=start
#include<queue>
using namespace std;
#if 0
class Solution {
//方法一：普通广度优先 bfs
private:
    struct Node {
        int x;
        int y;
        int step;
        Node(int i, int j, int s) : x(i), y(j), step(s) {}
    };  
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        queue<struct Node> q;
        int n = grid.size();
        if (n==0 || grid[0][0] || grid[n-1][n-1]) return -1;
        q.push(Node(0, 0, 1));
        grid[0][0] = 1;
        while (!q.empty()) {
            Node node = q.front();
            q.pop();
            if (node.x==n-1 && node.y==n-1) return node.step;
            for(int dx=-1; dx<=1; dx++) {
                for(int dy=-1; dy<=1; dy++) {
                    int i = node.x + dx;
                    int j = node.y + dy;
                    if(i<0 || j<0 || i>=n || j>=n || grid[i][j]) continue;
                    q.push(Node(i, j, node.step+1));
                    grid[i][j] = 1;
                }
            }
        }
        return -1;
    }
};
#endif
#if 1
//启发式搜索
int n;
struct Node {
    int x;
    int y;
    int step;
    Node (int x, int y, int s) : x(x), y(y), step(s){}
};
//自定义priority_queue的排列顺序.
//重载<，意思是B排在A前面，B是队顶。而内部的A>B， 又说明B是小元素，因此这里定义的是小顶队列
int heuristic(const Node A) {
    return max(n-1-A.x, n-1-A.y) + A.step;
}
bool operator < (const Node A, const Node B) {
    return heuristic(A) > heuristic(B);
}
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        n = grid.size();
        if (n == 0 || grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        if (n == 1) return 1;
        priority_queue<Node> q;
        q.push(Node(0, 0, 1));
        vector<int> stepList(n * n, 0);
        stepList[0] = 1;
        grid[0][0] = 1;
        vector<vector<int>> mov {{1, 1}, {1, 0}, {0, 1}, {-1, 1}, {1, -1}, {-1, 0}, {0, -1}, {-1, -1}};
        while (!q.empty()) {
            Node cur = q.top();  //优先队列，每次先取出队顶的优先节点
            q.pop();
            int curIdx = cur.x * n + cur.y;
            for (int k = 0; k < 8; ++k) {
                int xx = cur.x + mov[k][0];
                int yy = cur.y + mov[k][1];
                int nextIdx = xx * n + yy;
                if (xx < 0 || yy < 0 || xx >= n || yy >= n) continue;
                if (xx == n - 1 && yy == n - 1) return stepList[curIdx] + 1;
                // 没有走到过该点；或者之前走这个点比当前再走这个点的步数多，那就重新走这个点
                if (grid[xx][yy] == 0 || stepList[nextIdx] > stepList[curIdx] + 1) {
                    stepList[nextIdx] = stepList[curIdx] + 1;
                    Node next(xx, yy, cur.step + 1);
                    q.push(next);
                    grid[xx][yy] = 1;
                }
            }
        }
        return -1;
    }
};
#endif
// @lc code=end