#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#
'''
思路：
1.定义机器人四种基本行走步法，相对当前点，机器人向前、右、后、左走一步；
2.维护机器人运动方向状态，与基本步法相对应，用于指导机器人接下来怎么走；
3.执行运动命令：
3.1如果是转向命令，则改变上述运动方向状态，
3.2如果是行走命令，沿着当前方向一步步行走，判断机器人每个下一步位置是否与障碍物冲突：
   若冲突，不往下一步走了，结束本次运动命令；
   若不冲突，更新机器人位置到下一步；
4.每走一步，判断是否离原点更远，最后找到最远距离
'''

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        ans = 0
        #注意把list()的obstacle变为tuple，再变为set，便于查询是否存在某个元素
        ob_set = set([tuple(t) for t in obstacles])  #注意如何定义set()
        #定义候选方向的列表
        dd = [[0,1], [1,0],[0,-1],[-1,0]]
        #初始化方向为[0,1]
        dir = 0
        #初始化位置
        cur_pos = (0,0)
        for c in commands:
            if c == -2:
                dir = (dir+4-1) % 4
            if c == -1:
                dir = (dir+1) % 4
            for i in range(c):
                next_pos = (cur_pos[0]+dd[dir][0], cur_pos[1]+dd[dir][1])
                if next_pos in ob_set:
                    break
                cur_pos = next_pos
                ans = max(ans, cur_pos[0]*cur_pos[0]+ cur_pos[1]*cur_pos[1])
        return ans


# @lc code=end

