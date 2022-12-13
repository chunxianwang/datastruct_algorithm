#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, ans, tmp, unused):
            if len(tmp) == len(nums):
                ans.append(tmp[:])
                return
            for i in range(len(nums)):
                if unused[i]:
                    #搜索到这里的时候，当前节点nums[i]和前一个节点一样且前一个节点“可用”，那么就可能重复，需要剪枝
                    if i>0 and nums[i] == nums[i-1] and unused[i-1]:
                        continue
                    unused[i] = False
                    tmp.append(nums[i])
                    backtrack(nums, ans, tmp, unused)
                    unused[i] = True
                    tmp.pop()

        ans = list()
        tmp = list()
        unused = list()
        nums.sort()
        for i in range(len(nums)): unused.append(True)
        backtrack(nums, ans, tmp, unused)
        return ans
# @lc code=end

