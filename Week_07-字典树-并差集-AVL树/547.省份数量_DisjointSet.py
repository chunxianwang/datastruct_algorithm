#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 省份数量
#
'''
Disjoint-set
完整题解参考自: （含并查集完整知识讲解）
https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/

'''
# @lc code=start
class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        
        return uf.num_of_sets


# @lc code=end

