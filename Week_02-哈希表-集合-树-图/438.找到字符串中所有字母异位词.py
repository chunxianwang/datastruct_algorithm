#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        '''
        # 用字典
        dict_p = collections.defaultdict(int)
        np = len(p)
        for i in range(np):
            dict_p[p[i]] += 1
        
        dict_s = collections.defaultdict(int)
        ns = len(s)
        ans = list()
        for i in range(ns):
            dict_s[s[i]] += 1
            if i >= np:
                dict_s[s[i-np]] -= 1
                if dict_s[s[i-np]] == 0: dict_s.pop(s[i-np])  #清除value=0的key
            if i >= np-1 and dict_s == dict_p:
                ans.append(i-np+1)
        return ans
        '''
        
        # 用数组代替字典
        ans = list()
        list_p = [0] * 26
        list_s = [0] * 26
        np = len(p)
        for i in range(np):
            list_p[ord(p[i])- ord('a')] += 1
        ns = len(s)
        for i in range(ns):
            char = s[i]
            list_s[ord(char)- ord('a')] += 1
            if i >= np:
                list_s[ord(s[i-np])- ord('a')] -= 1
            if i >= np-1 and list_s == list_p:
                ans.append(i-np+1)
        return ans
# @lc code=end

