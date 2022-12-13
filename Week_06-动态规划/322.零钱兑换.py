#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #方法1，不带有备忘录的递归，会重复递归某些分之，超时错误
        ''''
        return dp(coins, amount)
        def dp(coins, amount):
            if amount == 0: return 0
            if amount < 0: return -1
            Min = float("inf")
            for coin in coins:
                subMin = dp(coins, amount-coin)
                if subMin==-1:
                    continue
                Min = min(Min, subMin+1)
            if Min == float("inf"): 
                return -1
            else:
                return Min
        
        '''
        #方法2，带备忘录的递归，自顶向下
        # 通过备忘录消除子问题，不会超时
        # dp备忘录数组全部初始化为特殊值
        
        memo = [-666] * (amount+1) #初始化定长度、带默认值的数组
        
        def dp(amount):
            if amount == 0: return 0
            if amount < 0: return -1
            #查询备忘录，避免重复计算
            if memo[amount] != -666:
                return memo[amount]
            Min = float("inf")
            for coin in coins:
                subMin = dp(amount-coin)
                if subMin==-1:
                    continue
                Min = min(Min, subMin+1)
            #把计算结果存入备忘录
            if Min == float("inf"): 
                memo[amount] = -1
            else:
                memo[amount] = Min
            return memo[amount]

        return dp(amount)
        

        #方法3：dp数组迭代-自底向上
        '''
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] == (amount+1):
            return -1
        else:
            return dp[amount]
        '''

# @lc code=end

