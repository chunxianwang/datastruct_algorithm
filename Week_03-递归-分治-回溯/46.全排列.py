#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, ans, tmp, unused):
            if len(tmp) == len(nums):
                ans.append(tmp)
                return
            for i in range(len(nums)):
                if unused[i]:
                    tmp.append(nums[i])
                    unused[i] = False
                    backtrack(nums, ans, tmp, unused)
                    unused[i] = True
                    tmp.pop()
            
        ans = list()
        unused = list()
        tmp = list()
        for i in range(len(nums)): unused.append(True)
        backtrack(nums, ans, tmp, unused)
        return ans

# @lc code=end

