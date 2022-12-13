#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#

# @lc code=start
# b站讲解版本的改进版，把xx1.py中的左闭右开改成了左闭环右闭

class Solution(object):
    #将[begin, mid) 和 [mid, end) 范围的数组合并成一个有序数组
    def merge(self, nums, begin, mid, end):
        #备份左边数组
        leftnums = []
        for i in range(mid-begin):
            leftnums.append(nums[begin+i])
        
        li = 0         #指向备份数组起始位置
        le = mid-begin #备份数组长度
        ri = mid       #指向右边数组起始位置
        re = end       #指向右边数组结束位置
        wi = begin     #指向待写入地址

        # 记住，左右半边数据内部分别是有序的
        # 这时，需要遍历备份的左半边数据
        # 意味着左半边一旦遍历结束，右半边就不需要再做任何操作
        while li < le:
            #左半边没结束又分为两种情况
            # 情况一是右半边也没结束且左元素大于右元素    ->     要写入右元素
            if ri < re and nums[ri] < leftnums[li]:
                nums[wi] = nums[ri]
                wi += 1
                ri += 1
            #情况二是右半边已经结束或者左元素小于右元素   ->     要写入左元素
            else:
                nums[wi] = leftnums[li]
                wi += 1
                li += 1
    
    def sort(self, nums, begin, end):
        if end - begin < 2: 
            return
        #分割成左右两部分待排序数组
        mid = (begin+end)//2
        self.sort(nums, begin, mid)
        self.sort(nums, mid, end)
        self.merge(nums, begin, mid, end)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.sort(nums, 0, len(nums)) #左闭右开
        return nums
    
# @lc code=end