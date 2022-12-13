#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 省份数量
#
'''
DFS
解题想法
1. 每到一个城市 将其所在省份的城市纳入visited
2. 到达一个城市 不在visited说明这属于一个新的省份 num_prov+1
重要细节：
dfs中没有显式写什么时候return 但是j加入visited时需要判断 if j not in visited。
这自然的给出return的一个条件: dfs(i)时, 若i的邻居都在visited中, 则return。
(没有一个 j 进入 dfs(j))
'''
# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        cities = len(isConnected)
        # 递归搜索i所在省份的其它城市，都加入到visited中
        def dfs(i):
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        num_prov = 0
        #遍历所有城市
        for i in range(cities):
            #如果i不在之前遍历过的城市
            if i not in visited: num_prov += 1
            #递归搜索，将i所在省份的其它城市都纳入visited
            dfs(i)
        return num_prov


# @lc code=end

