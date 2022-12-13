#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#
'''
//正向: 遍历数组，维护当前位置最远可达边界maxPos; 
//     维护‘当前步’的最远可达位置，如果到达，则步数+1，且更新‘当前步’的最远可达位置；
//     注意：题目中有能到达最远位置的前提条件，在遍历数组时，我们不访问最后一个元素， 即i<nums.size()-1；
//          这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
//          如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，
//          因此我们不必访问最后一个元素。
'''

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxpos = 0
        end = 0
        steps = 0
        for i in range(len(nums)-1):
            maxpos = max(maxpos, i+nums[i])
            if i == end:
                steps += 1
                end = maxpos
        return steps

# @lc code=end

