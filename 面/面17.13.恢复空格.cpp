/*

哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。
当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
注意：本题相对原题稍作改动，只需返回未识别的字符数
*/



class Trie {
public:
    //26个字母，对应26个分支节点
    Trie* next[26] = {nullptr};
    //用于标记单词结束
    bool isEnd;
    Trie() {
        isEnd = false;
    }
    //插入一个单词字符串
    void insert(string word) {
        //从根节点开始插入单词
        Trie* curPos = this;
        //技巧：倒序查询单词，那就把单词倒序插入字典树
        for (int i = word.length() - 1; i >= 0; --i) {
            int t = word[i] - 'a';
            if (curPos->next[t] == nullptr) {
                curPos->next[t] = new Trie();
            }
            curPos = curPos->next[t];
        }
        //标记单词结束
        curPos->isEnd = true;
    }
};

class Solution {
public:
    int respace(vector<string>& dictionary, string sentence) {
        int n = sentence.length(), inf = 0x3f3f3f3f;
        //由词典创建字典树
        Trie* root = new Trie();
        for (auto& word: dictionary) {
            root->insert(word);
        }
        //动态规划dp[i] 0~i-1范围内（即前i个字符）未识别字符的数量
        vector<int> dp(n + 1, inf);
        dp[0] = 0;
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i - 1] + 1;

            Trie* curPos = root;
            for (int j = i; j >= 1; --j) {
                int t = sentence[j - 1] - 'a';
                if (curPos->next[t] == nullptr) {
                    break;
                } else if (curPos->next[t]->isEnd) {  //j-1 ～ i-1范围的字符是一个合法单词

                    dp[i] = min(dp[i], dp[j - 1]);
                }
                if (dp[i] == 0) {
                    break;
                }
                curPos = curPos->next[t];
            }
        }
        return dp[n];
    }
};