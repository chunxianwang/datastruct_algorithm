#
# @lc app=leetcode.cn id=403 lang=python
#
# [403] 青蛙过河
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        '''
        #普通dfs，超时报错
        def dfs(pos,step):
            if pos==stones[-1]: return True
            for d in [-1,0,1]:
                if step+d>0 and pos+step+d in set(stones):
                    if dfs(pos+step+d, step+d):
                        return True
            return False
        pos, step = 0, 0
        return dfs(pos, step)
        '''

        # 动态规划
        # 定义dp为字典，其中key=stone, value={可以到达的跳跃步长组成的集合},
        # 那么能够到达stone等价于dp[stone]非空。
        set_stones = set(stones)
        dp = defaultdict(set)
        dp[0] = {0}
        for s in stones:
            for step in dp[s]:
                for d in [-1, 0, 1]:
                    if step+d > 0 and s+step+d in set_stones:
                        dp[s+step+d].add(step+d)
        return len(dp[stones[-1]]) > 0

# @lc code=end

