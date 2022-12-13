/*
 * @lc app=leetcode.cn id=104 lang=cpp
 *
 * [104] 二叉树的最大深度
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
#if 1
//深度优先：递归版
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;
        return max(maxDepth(root -> left), maxDepth(root -> right)) + 1;
    }
};
#endif

#if 0
//深度优先：迭代，用栈
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0;
        stack<pair<TreeNode*,int>> s;
        TreeNode* p=root;
        int Maxdeep=0;
        int deep=0;
        while(!s.empty()||p!=NULL)//若栈非空，则说明还有一些节点的右子树尚未探索；若p非空，意味着还有一些节点的左子树尚未探索
        {
            while(p!=NULL)//优先往左边走
            {
                s.push(pair<TreeNode*,int>(p,++deep));
                p=p->left;
            }
            p=s.top().first;//若左边无路，就预备右拐。右拐之前，记录右拐点的基本信息
            deep=s.top().second;
            if(Maxdeep<deep) Maxdeep=deep;//预备右拐时，比较当前节点深度和之前存储的最大深度
            s.pop();//将右拐点出栈；此时栈顶为右拐点的前一个结点。在右拐点的右子树全被遍历完后，会预备在这个节点右拐
            p=p->right;
        }
        return Maxdeep;
    }
};
#endif

#if 0
//广度优先：迭代，使用队列
class Solution {
public:
    int maxDepth(TreeNode* root) {
         if(root==NULL) return 0;
         deque<TreeNode*> q;
         q.push_back(root);
         int deep=0;
         while(!q.empty())
         {
             deep++;
             int num=q.size();
             for(int i=1;i<=num;i++)
             {
                TreeNode* p=q.front();
                q.pop_front();
                if(p->left) q.push_back(p->left);
                if(p->right) q.push_back(p->right);
             }
         }
         return deep;         
    }
};
#endif



// @lc code=end

