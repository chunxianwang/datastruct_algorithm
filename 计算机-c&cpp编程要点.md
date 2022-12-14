撰写目标：
1. 总结数据结构与算法练习中涉及的常见编程要点，包括技巧、规范等；
2. 方便回顾掌握c&c++的书写习惯；

### 1. 引用作为函数参数-避免大数据块拷贝
函数参数传递三种方式：
1. 值传递        函数内部对参数的操作，不能影响函数外部的实参；要想实现影响，只能通过return返回值来实现。
2. 指针传递参数   函数内部对参数的操作，会影响函数外部的实参；
3. 引用传递参数   函数内部对参数的操作，会影响函数外部的实参；
```c++
#include <iostream>
using namespace std;
int main( )
{
   //声明3种参数传递函数
   void swap1(int,int); 
   void swap2(int *,int *);
   void swap3(int &,int &);

   int i=3,j=5;
   swap1(i,j); 
   cout<<i<<" "<<j<<endl;  //输出i=3，j=5，实际上值未互换
   swap2(&i,&j);  //实参是变量的地址
   cout<<i<<" "<<j<<endl;  //输出i=5和j=3,值已互换
   swap3(i,j);
   cout<<"i="<<i<<"  "<<"j="<<j<<endl; //输出i=3，j=5，值又被换回
   return 0;
}
//值传递参数
void swap1(int a,int b)  //企图通过形参a和b的值互换,实现实参i和j的值互换
{
   int temp;
   temp=a;  
   a=b;
   b=temp;
}
//指针传递参数
void swap2(int *p1,int *p2)  //形参是指针变量
{
   int temp;
   temp=*p1;  
   *p1=*p2;
   *p2=temp;
}
//引用传递参数
void swap3(int &a,int &b)  //形参是引用类型
{
   int temp;
   temp=a;
   a=b;
   b=temp;
}
```
引用的常见用法：引用传递数组，避免大数据块拷贝
如应用题目：
[](Week_02/94.二叉树的中序遍历.cpp)
```c++
void inorder(TreeNode* root, vector<int>& res) {  //引用数组作为函数参数，函数内部的操作，直接对函数外实参产生影响，避免用return结果的方法传递大数据块。
    if(!root) {
        return; //仅作退出，不用来返回结果；
    }
    inorder(root->left, res);
    res.push_back(root->val);
    inorder(root->right, res);
}
```
