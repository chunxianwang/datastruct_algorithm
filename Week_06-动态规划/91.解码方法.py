#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

'''
 * 内核为非波拉契数列的动态规划问题，特点是需要考虑的情况比较多
 * 
 * s[i] 为字符串s的第i个字符，f(i)表示到s[i]一共有多数种解码方式
 * 
 * if(s[i]=='0') 
 *     if (s[i-1]=='1' || s[i-1]=='2') -->f(i)=f(i-2)
 *        //就是说，最后两位只能合并解码为10 或20， 例如1212120，
 *        //解码的数量和12121相同（最后两位20是唯一解，解码总数不增加。）；
 *     else -->return 0;
 *        //字符串非法，，就是说0只能出现在1或2的后面，组成10或20，如果是30、40...，那就不能正常解码了
 * if(s[i]!='0')
 *      if(s[i-1]==1 || (s[i-1]==2 &&1<=s[i]<=6)) -->f(i) = f(i-1) + f(i-2)
 *         //就是最后两位在11-26之间，如1212121，可以翻译为12121+21或121212+1
 *      else --> f(i) = f(i-1);
 *         //就是最后两位不再11到26之间，如1212132，只能翻译成121213+2

'''

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        n = len(s)
        dp = [1] * (n+1)
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            if s[i] != '0':
                if s[i-1] == '1' or (s[i-1]=='2'and s[i]>='1'and s[i]<='6'):
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[n]

# @lc code=end

