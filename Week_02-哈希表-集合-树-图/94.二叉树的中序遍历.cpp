/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include<vector>
using namespace std;
class Solution {
public:
#if 0


#if 1
//标准的递归写法
    void inorder(TreeNode* root, vector<int>& res) {
        //退出当前层
        if(!root) {
            return;
        }
        //进入到下一层
        inorder(root->left, res);
        //处理当前层逻辑
        res.push_back(root->val);
        //进入到下一层
        inorder(root->right, res);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        //进入递归的入口
        inorder(root, res);
        return res;
    }
#endif
    /*
    栈迭代方法思路：
    中序遍历
    每到一个节点 A，因为根的访问在中间，将 A 入栈。
    然后遍历左子树，接着访问 A，最后遍历右子树。
    在访问完 A 后，A 就可以出栈了。因为 A 和其左子树都已经访问完成。
    伪代码：
    初始化根节点
    枚举更新根节点，来自栈中暂存各级根节点的右子树
        枚举更新根节点，来自上次循环中根节点的左子树
            栈中暂存右子树；
        根节点指向当前根的左子树
    根节点指向栈顶暂存根节点的右子树，弹栈顶；
    输出根节点的值；
    更新根节点为栈中弹出根节点的右子树
    */
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> ans;
        while(root != nullptr || !st.empty()){
            while(root!=nullptr){
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            ans.push_back(root->val);
            root = root->right;
        }
        return ans;        
    }
};
// @lc code=end

