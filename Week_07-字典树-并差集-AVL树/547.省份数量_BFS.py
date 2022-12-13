#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 省份数量
#
'''
BFS
解题想法

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
        num_prov = 0
        for i in range(cities):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(cities):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                num_prov += 1
        return num_prov


# @lc code=end

