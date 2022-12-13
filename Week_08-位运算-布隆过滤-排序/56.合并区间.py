#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#
'''
* 首先，将列表中的区间按照左端点升序排序。然后将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
* 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，可以直接将这个区间加入数组 merged 的末尾；
* 否则，它们重合，需要用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。
'''

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])  #数组排序
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # 否则的话，就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
# @lc code=end

