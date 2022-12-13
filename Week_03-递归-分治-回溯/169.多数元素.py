#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # 方法1:哈希表方法
        # 建立哈希表时，同步进行打擂台，维护出现次数最多的元素及其出现次数
        dictable = dict()
        cnt = 0
        for i in range(len(nums)):
            if nums[i] in dictable:
                dictable[nums[i]] += 1
            else:
                dictable[nums[i]] = 1
            if dictable[nums[i]] > cnt:
                majority = nums[i]
                cnt += 1
        return majority
        '''
        #方法2，候选多数元素打擂台
        #假定当前元素是候选多数元素，遍历后续元素并对其计数
        #如果和候选元素相同，计数+1
        #如果和候选元素不同，技术减1，如果减到了0，说明其可能不是候选多数元素，则把当前元素列为候选多数元素，从1开始对其进行计数
        #遍历结束，最后的候选元素即为结果
        target = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != target:
                cnt -= 1
                if cnt == 0:
                    target = nums[i]
                    cnt = 1
            else:
                cnt += 1
        return target

        
# @lc code=end

