#
# @lc app=leetcode.cn id=299 lang=python
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cntS, cntG = [0]*10, [0]*10
        for i in range(min(len(secret), len(guess))):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                cntS[int(secret[i])] += 1
                cntG[int(guess[i])] += 1
        cows = sum(min(s,g) for s, g in zip(cntS, cntG))
        return str(bulls)+'A'+str(cows)+'B'
        

        

# @lc code=end

