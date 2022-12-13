#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = list()
        #回溯
        def backtrack(tmp, index):
            #遇到所有数字号码都列举结束，就把字符串加入结果列表并返回
            if index == len(digits):
                ans.append(tmp)
                return
            else:
                digit = digits[index]
                letters = phoneMap[digit]
                for i in letters:
                    backtrack(tmp+i, index+1)
        backtrack("", 0)
        return ans


# @lc code=end

