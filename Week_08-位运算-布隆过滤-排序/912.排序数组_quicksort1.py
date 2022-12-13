#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#

# @lc code=start
# b站讲解版本

class Solution(object):
    #构造出[begin, end)范围的轴点元素
    def pivotIndex(self, nums, begin, end):
        #end指向最后一个元素
        end -= 1
        #随机选择一个元素作为轴点，跟begin位置进行交换
        pivotindex = random.randint(begin, end)
        nums[pivotindex], nums[begin] = nums[begin], nums[pivotindex]
        #备份begin位置的元素，便于后续本地转移各元素
        pivot = nums[begin]
        while begin < end:
            while begin < end:  #从右往左方向
                if nums[end] > pivot: #右元素 > 轴点元素，继续遍历右元素的下一个（往左方向）
                    end -= 1
                else:                 #要点：如果右元素 <= 轴点元素（这里包含等于的情况），那就交换到begin，begin右移并换方向
                    nums[begin] = nums[end]  
                    begin += 1
                    break
            while begin < end:  #从左往右方向
                if nums[begin] < pivot:   #左元素 < 轴点元素，继续遍历左元素的下一个（往右方向）
                    begin += 1
                else:
                    nums[end] = nums[begin]   
                    end -= 1
                    break
        #轴点数据放到合适的轴点位置，并范围轴点索引位置
        nums[begin] = pivot
        return begin
    
    def sort(self, nums, begin, end):
        if (end-begin) < 1:    #数组每一个元素都变成pivot，就退出递归
            return
        mid = self.pivotIndex(nums, begin, end)
        self.sort(nums, begin, mid)  #左闭右开
        self.sort(nums, mid+1, end)  #左闭右开

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.sort(nums, 0, len(nums)) #左闭右开
        return nums
    
# @lc code=end