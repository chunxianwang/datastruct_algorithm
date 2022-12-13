#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank:
            return -1
        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "ACT",
            "T": "CGA",
        }
        min_count = len(bank) + 1
        def dfs(current, count, current_bank, min_count):
            #nonlocal min_count
            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank: #穷举bank依然没有找到end -> 结束
                return
            
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i+1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    dfs(new, count+1, current_bank, min_count)
        dfs(start, 0, bank, min_count)
        return min_count if min_count <= len(bank) else -1

# @lc code=end

