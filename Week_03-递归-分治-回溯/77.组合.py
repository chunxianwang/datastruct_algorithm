#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = list()
        path = list()
        # DFS
        # 已取的为temp 从剩下[cur..n]区间中取或不取数 直到temp有k个元素
        def dfs(tmp, cur):
            # 如果加上剩下的也取不够k个（之前不取的太多了） 直接剪枝
            if len(tmp) + n - cur + 1 < k:
                return
            # 如果已经取够了
            if len(tmp) == k:
                ans.append(tmp)
                return
            #情况1:不选取当前位置  （深度优先）
            dfs(tmp, cur+1)
            #情况2:选取当前位置
            dfs(tmp+[cur], cur+1)
        dfs([], 1)
        return ans
# @lc code=end

