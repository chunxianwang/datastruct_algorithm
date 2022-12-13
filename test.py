# git branch test
import collections
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        left, right = 0, 0
        matched_char_num = 0
        start = 0
        length = len(s) + 1
        while right < len(s):
            print('hello0')
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    matched_char_num += 1
            while matched_char_num == len(need):
                print('hello1')
                if right - left < length:
                    start = left
                    length = right-left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        matched_char_num -= 1
                    window[d] -= 1
        if length == len(s) + 1:
            return ''
        else:
            print(start)
            return s[start:start+length]

class Solution2:
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
            print('hello0')
            c = s[right] # 即将加入window的字符c
            right += 1 # 右移窗口

            # 窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]: # window中字符c出现的次数已经达到need所需要的次数时，valid进行更新
                    matched_char_num += 1

            # 判断窗口左侧边界是否要收缩
            while matched_char_num == len(need):
                print('hello1')
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
            print(start)
            return s[start:start+length]

s = 'aab'
t = 'aab'

solution = Solution1

print(solution.minWindow(s,s,t))
