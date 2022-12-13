#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = list()
        nums.sort()
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]: continue
            for b in range(a+1, len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]: continue
                c = b+1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum > target:
                        d -= 1
                    if sum < target:
                        c += 1
                    #注意如何组织代码来处理重复
                    if sum == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]: c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]: d -= 1
        return ans
                        

# @lc code=end

