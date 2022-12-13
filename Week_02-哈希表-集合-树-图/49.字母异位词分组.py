#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
# 关键词：字典
#

# @lc code=start


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #核心思想：利用字典，key是字母重排序后的string，value是包含原string的数组
        '''
        dictable = dict()
        for s in strs:
            key = ''.join(sorted(s)) #对string中的characters排序
            if key in dictable:
                dictable[key].append(s)
            else:
                dictable[key] = [s]
        return [v for v in dictable.values()]
        '''
        dictable = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dictable[key].append(s)
        return [v for v in dictable.values()]

# @lc code=end

