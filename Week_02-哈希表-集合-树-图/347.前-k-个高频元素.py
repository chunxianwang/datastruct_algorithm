#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
######
#本题目主要用到数据结构“堆”
#详细请参考：[数据结构：堆（Heap）](https://www.jianshu.com/p/6b526aa481b1)

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就"一直"下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就"一直"上浮"""
            val = arr[child]
            #如果有父节点，且新节点<父节点，就上浮，且用循环实现可持续上浮
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1) 
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1) 
        return [item[0] for item in heap[1:]]
        
# @lc code=end

