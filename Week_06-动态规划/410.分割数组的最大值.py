#
# @lc app=leetcode.cn id=410 lang=python
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # 方法1，二分法+贪心
        # 选定一个x，可以验证是否存在一种分割方案，满足其最大分割子数组的和不超过x。
        # 验证策略采用贪心法：贪心地模拟分割的过程，从前到后遍历数组，用 sum 表示当前分割子数组的和，cnt 表示已经分割出的子数组的数量（包括当前子数组），
        #     那么每当 sum 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1。遍历结束后验证是否 cnt 不超过 m。
        # 这样就可以用二分查找来找到x：二分的上界为数组 nums 中所有元素的和，
        # 下界为数组 nums 中所有元素的最大值。通过二分查找，我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。
        def check(x):
            total = 0
            cnt = 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

