#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        nums.sort()
        for a in range(len(nums)-2):
            if nums[a] > 0: break
            if a>0 and nums[a]==nums[a-1]: continue
            b = a+1
            c = len(nums)-1
            while b < c:
                sum = nums[a] + nums[b] + nums[c]
                if sum == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while b<c and nums[b]==nums[b-1]: b+=1
                    c -= 1
                    while b<c and nums[c]==nums[c+1]: c-=1
                if sum>0: c-=1
                if sum<0: b+=1
        return ans

# @lc code=end

