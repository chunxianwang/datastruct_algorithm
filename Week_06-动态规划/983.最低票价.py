#
# @lc app=leetcode.cn id=983 lang=python
#
# [983] 最低票价
#

# @lc code=start
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        N = len(days)
        durations = [1, 7, 30]

        def dp(i):
            if i >= N:
                return 0
            ans = 10**9
            j = i
            for c, d in zip(costs, durations):
                # 只要是不超过本次付钱所能使用的期限，就免费使用，即暂不付费
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0)
        
# @lc code=end

