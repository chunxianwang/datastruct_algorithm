# 极客大学「算法训练营-第8期」作业提交仓库


## 讲师课件下载地址

请大家通过该链接查看讲师课件并进行下载，链接:https://pan.baidu.com/s/1DM7UAhSYs3Im_t2ayiAAXQ  密码:9fct


## 仓库目录结构说明

1. `week01/` 代表第一周作业提交目录，以此类推。
2. 请在对应周的目录下新建或修改自己的代码作业。
2. 每周均有一个 `NOTE.md` 文档，你可以将自己当周的学习心得以及做题过程中的思考记录在该文档中。

## 作业提交规则
 
1. 先将本仓库 Fork 到自己 GitHub 账号下。
2. 将 Fork 后的仓库 Clone 到本地，然后在本地仓库中对应周的目录下新建或修改自己的代码作业，当周的学习总结写在对应周的NOTE.md文件里。
3. 在本地仓库完成作业后，push 到自己的 GitHub 远程仓库。
4. 最后将远程仓库中当周的作业链接，按格式贴到班级仓库对应学习周的issue下面。
5. 提交issue请务必按照规定格式进行提交，否则作业统计工具将抓取不到你的作业提交记录。 


## 注意事项
 如果对 Git 和 GitHub 不太了解，请参考 [Git 官方文档](https://git-scm.com/book/zh/v2) 或者极客时间的[《玩转 Git 三剑客》](https://time.geekbang.org/course/intro/145)视频课程。

 ## 刷题流程
 1. 新题入库管理：新题目在网页leetcode通过收藏进行管理
 2. 五毒神掌之一，整理题解笔记：在vscode-leetcode默认工作区整理题解，存入algorithm文件夹weekx
 3. 五毒神掌之2～5:在vscode-leetcode打开题目默认coding界面进行练习

## 模板题目合集
### 1.DFS

----
## 牛客网输入输出方式
万变不离其宗：虽然可以直接用cin>>n，但是为了及时处理输入错误，往往把输入（如果多于一个输入的第一个输入）放到while()中，如果出错，及时结束。比如要求输入int，你用键盘敲入了一个字符'b'，那就是输入错误。
1. 输入数字
   ```c++
   int n;
   while(cin>>n) {
       //processing with n;
   }
   ```
2. 输入确定尺寸的数组
   ```c++
   int n;
   while(cin>>n) {
       for(int i = 0; i < n; i++) {
           cin>>std[i].name>>stu[i].num;
       }
   }
   ```
3. 输入数组，不确定尺寸
   ```c++
   vector<student> Input;
   int n;
   while(cin>>name>>num) {
       student s = {name, num};
       Input.push_back(s);
   }
   ```

4. 输入字符（串）
   ```c++
   char ch;
   while(cin.get(ch)) {
       //processing with ch;
   }
   //字符串
   string st;
   //方法一
   while(getline(cin, st)) {
       //processing with st;
   }
   //方法二
   while(cin>>st) {
       //processing with st;
   }
   ```

5. 输入（确定尺寸的）字符串数组
   ```c++
   string st;
   int n;
   while(cin>>n) {
       vector<string> input;
       for(int i = 0; i < n; i++) {
           cin>>st;
           input.push_back(st);
       }
   }
   ```

6. 输入（不确定尺寸的）字符串数组
   ```c++
   string st;
   vector<string> input;
   while(cin>>st) {
       input.push_back(st);
   }
   ```

输出用cout，当多个输出结果时，注意使用换行符，如：
cout<<input<<endl;