#
# @lc app=leetcode.cn id=493 lang=python
#
# [493] 翻转对
# 参考官方题解，参照c++版本改写而成
# 思路：归并排序


# @lc code=start
class Solution(object):
    def reversePairsRecursive(self, nums, left, right):
        if left == right:
            return 0
        else:
            mid = (left + right) // 2
            n1 = self.reversePairsRecursive(nums, left, mid)
            n2 = self.reversePairsRecursive(nums, mid+1, right)
            ret = n1 + n2
        # 首先统计下标对的数量
        i, j = left, mid + 1
        while i <= mid:
            while j <= right and nums[i] > 2* nums[j]:
                j += 1
            ret += (j - mid -1)
            i += 1
        
        # 随后合并两个排序数组
        sorted = [0 for _ in range(right-left+1)]
        p1, p2 = left, mid + 1
        p = 0
        while p1<=mid or p2<=right:
            if p1 > mid:
                sorted[p] = nums[p2]
                p += 1
                p2 += 1
            elif p2 > right:
                sorted[p] = nums[p1]
                p += 1
                p1 += 1
            else:
                if nums[p1] < nums[p2]:
                    sorted[p] = nums[p1]
                    p += 1
                    p1 += 1
                else:
                    sorted[p] = nums[p2]
                    p += 1
                    p2 += 1
        for i in range(len(sorted)):
            nums[left+i] = sorted[i]
        return ret

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.reversePairsRecursive(nums, 0, len(nums)-1)

# @lc code=end

