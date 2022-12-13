/*
 * @lc app=leetcode.cn id=621 lang=cpp
 *
 * [621] 任务调度器
 */
/*
对所有任务做个统计，找出出现次数最多的任务（一个或多个），它（们）的出现次数maxExec，以及它（们）的个数maxCount。

对于重复的任务，我们只能将每个都放入不同的桶中，因此桶的个数就是重复次数最多的任务的个数。

一个桶不管是否放满，其占用的时间均为 n+1，这是因为后面桶里的任务需要等待冷却时间。
最后一个桶是个特例，由于其后没有其他任务需等待，所以占用的时间为桶中的任务个数。

最终得到：

总排队时间 = (maxExec - 1) * (n + 1) + maxCount

最后，当任务重复率很低时，即任务种类数大于桶尺寸n-1时，可能出现桶就放不下这么多种类任务。
此时可以假想在最后一桶之后又补充了很多个桶，且所有的桶均装满，因此任务的总等待时间即为任务的总个数。
*/

// @lc code=start
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int>cnt(26,0);
        for(auto type : tasks)  // 桶排序思想
            cnt[type-'A']++;
        int cnt_max = 0, equal_cnt_max = 0;  //
        for(auto i: cnt) cnt_max = max(i, cnt_max);  //次数最多任务的出现次数
        for(int i = 25; i>=0; --i) 
            if(cnt_max == cnt[i])
                ++equal_cnt_max;  // 统计出现次数最多的任务总个数
        int ans = max((n+1)*(cnt_max-1) + equal_cnt_max, (int)tasks.size());
        return ans;
    }
};
// @lc code=end

