#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水：数组、双指针
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        #方法1
        #核心思想：更新维护左、右侧最高高度
        left = 0
        right = len(height)-1
        ans = 0
        maxheight_left = 0 
        maxheight_right = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxheight_left:
                    maxheight_left = height[left]
                else:
                    ans += (maxheight_left - height[left])
                left += 1
            else:
                if height[right] >= maxheight_right:
                    maxheight_right = height[right]
                else:
                    ans += (maxheight_right-height[right])
                right -= 1
        return ans
        '''
        #方法2: 
        n = len(height)
        leftmaxheight = [0 for i in range(n)]
        leftmax = 0
        for i in range(n):
            leftmax = max(leftmax, height[i])
            leftmaxheight[i] = leftmax
        
        rightmaxheight = [0 for i in range(n)]
        rightmax = 0
        for j in range(n-1, -1, -1):
            rightmax = max(rightmax, height[j])
            rightmaxheight[j] = rightmax
        sum = 0
        for i in range(n):
            sum += (min(leftmaxheight[i], rightmaxheight[i])-height[i])
        return sum


# @lc code=end

