/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */
// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
#if 0
/*
哈希表存储各个元素出现次数；
方法一：遍历哈希表，看哪个元素出现次数多；
方法二：建立哈希表时，同步进行打擂台，维护出现次数最多的元素及其出现次数
*/       
        int majority;
        unordered_map<int,int> um;
        int cnt = 0;
        for (auto n : nums) {
            um[n]++;
            if (um[n] >cnt) {
                majority = n;
                cnt = um[n];
            }
        }
        return majority;
#endif
#if 1
/*
原理，假定第一个元素是多数元素，遍历后续所有元素，出现和当前假定多数元素相同的元素，+1；不同的元素，-1；
如果当前假定元素的计数等于0，则其可能不是多数元素，变更假定多少元素为当前遍历到的元素
遍历结束，最后的假定多数元素是真的多数元素
*/
        int target = nums[0];
        int count = 1;
        for(int i = 1;i<nums.size();i++){
            if(nums[i]!=target) {  
                count--;
                if(count==0)
                {
                    target = nums[i];
                    count = 1;
                }
            } else count++;
        }
        return target;
#endif
    }

};
// @lc code=end

