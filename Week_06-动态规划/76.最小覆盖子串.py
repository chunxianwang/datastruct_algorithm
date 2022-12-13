#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#【参考解答】https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
'''
滑动窗口的思想：

用i,j表示滑动窗口的左边界和右边界，通过改变i,j来扩展和收缩滑动窗口，可以想象成一个窗口在字符串上游走，当这个窗口包含的元素满足条件，即包含字符串T的所有元素，记录下这个滑动窗口的长度j-i+1，这些长度中的最小值就是要求的结果。

步骤一

不断增加j使滑动窗口增大，直到窗口包含了T的所有元素

步骤二

不断增加i使滑动窗口缩小，因为是要求最小字串，所以将不必要的元素排除在外，使长度减小，直到碰到一个必须包含的元素，这个时候不能再扔了，再扔就不满足条件了，记录此时滑动窗口的长度，并保存最小值

步骤三

让i再增加一个位置，这个时候滑动窗口肯定不满足条件了，那么继续从步骤一开始执行，寻找新的满足条件的滑动窗口，如此反复，直到j超出了字符串S范围。
'''

# @lc code=start
import collections
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #用need字典保存t中的所有元素
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        
        needCnt=len(t)
        i=0   #记录窗口起始位置
        res=(0,float('inf'))  #用tuple记录满足要求窗口的起、终点，开始时把终点设为无穷远
        #三步骤
        #1. 扩张右边界，使滑窗包含t        ！注意，处理的是j
        for j,c in enumerate(s):
            #如果在s中找到了一个t的元素，t的待查找长度减1
            if need[c]>0:
                needCnt-=1
            need[c]-=1
        #2. 收缩左边界，直到无法再去掉元素   !注意，处理的是i
            if needCnt==0:       
                while True:      
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #更新记录满足要求窗口的起、终点
                    res=(i,j)
        #3. i向后移动1个位置，准备开始下一次循环(注意这步是在 needCnt == 0里面进行的 )
                need[s[i]]+=1  #在移动前，i这个位置一定是所需的字母，因此需要把它恢复到need字典里
                needCnt+=1  #在移动前，i这个位置一定是所需的字母，因此NeedCnt需要+1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
'''


## labuladong 滑动窗口框架方法
class Solution:
    def minWindow(self, s, t):
        need = collections.defaultdict(int) # 记录t中字符出现次数
        window = collections.defaultdict(int) # 记录窗口中相应的字符出现的次数
        for c in t:
            need[c] += 1
        
        left,right = 0,0 # 初始窗口长度为0
        matched_char_num = 0 # 用于记录window中已经出现的与t中字符数相同的字符个数，比如：t='abc'，window='abd',valid就等于2.代表need中应该出现的字符在window中才出现了两个，还没有出现完全

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = len(s) + 1  # 初始化成一个较大值， 这里相当于intmax

        while right < len(s):    #[left, right) 左闭右开窗口
            c = s[right] # 即将加入window的字符c
            right += 1 # 右移窗口

            # 窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]: # window中字符c出现的次数已经达到need所需要的次数时，valid进行更新
                    matched_char_num += 1

            # 判断窗口左侧边界是否要收缩
            while matched_char_num == len(need):
                # 在这里更新最小覆盖子串：起始索引，长度
                if right-left < length:
                    start = left
                    length = right-left

                # d是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]: # 这句话和下面的window[c]-=1不能反，先判断删去的字符c的数量是不是满足need的数量，如果满足，valid将减去1。
                        matched_char_num -= 1
                    window[d] -= 1
        # 返回最小覆盖子串
        if length == len(s) + 1:
            return ''
        else:
            return s[start:start+length]

# @lc code=end

