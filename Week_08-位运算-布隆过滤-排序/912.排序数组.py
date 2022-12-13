#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#

# @lc code=start

class Solution(object):
    
    def randomized_partition(self, nums, begin, end):
        pivotindex = random.randint(begin, end)
        #标杆值交换到最右侧
        nums[pivotindex], nums[end] = nums[end], nums[pivotindex]
        #遍历查看是否大于标杆值，用双指针，i指向放置小于标杆值的数据的位置，j指向遍历数据的位置
        i = begin
        for j in range(begin, end):
            if nums[j] < nums[end]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        #确定标杆值的合适位置，并从最右侧交换到这个合适位置
        pivotindex = i
        nums[pivotindex], nums[end] = nums[end], nums[pivotindex]
        return pivotindex

    def randomized_quicksort(self, nums, begin, end):
        if end - begin <= 0:
            return
        mid = self.randomized_partition(nums, begin, end)
        self.randomized_quicksort(nums, begin, mid - 1)
        self.randomized_quicksort(nums, mid + 1, end)
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.randomized_quicksort(nums, 0, len(nums)-1) #左闭右闭
        return nums
        
    
# @lc code=end