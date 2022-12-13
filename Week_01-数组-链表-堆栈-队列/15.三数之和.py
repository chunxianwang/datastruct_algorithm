#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和：三指针
#解体思路：
# 先对数组排序，然后用三个指针，第一个是枚举target的指针，后面两个是左右指针；
# 这三个指针都要考虑数组中元素重复的情况
# 时间复杂度：O(N^2)

#进一步分析
# 如果枚举3个数，时间复杂度是O(N^3)，那么降低到时间复杂度为O(N^2)的根本原因是什么呢？
# 其实是排序
# 排序后才能用左右指针的一个循环代替最原始三层循环的后两层
# 同时排序后也方便去除重复
# 另外排序本身的时间复杂度是O(NlogN)

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        # 代码风格1,第二层循环的内部逻辑略乱，不推荐
        n = len(nums)
        nums.sort()
        ans = list()
        for first in range(n-2):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first+1, n-1):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans
        '''

        # 代码风格2: 第二个循环中的逻辑更清晰：如果三数之和等于0，且左或右元素重复，则循环，不断向中心移动左右指针，直到不再重复
        n = len(nums)
        nums.sort()
        ans = list()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                # 三数之和的三种基本情况：等于0（考虑去重），大于0（right指针左移），小于0（left指针右移）
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
        return ans

# @lc code=end

