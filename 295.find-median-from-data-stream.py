#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
import heapq
# @lc code=start
class MedianFinder:

    def __init__(self):
        self.left_heap = list()
        self.right_heap = list()

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)
        heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        if len(self.left_heap)<len(self.right_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.left_heap)>len(self.right_heap):
            return -self.left_heap[0]
        return (-self.left_heap[0]+self.right_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
from utils import test
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    test(mf.findMedian(),1)
    mf.addNum(2)
    test(mf.findMedian(),1.5)
    mf.addNum(3)
    test(mf.findMedian(),2)
    mf.addNum(4)
    test(mf.findMedian(),2.5)
    mf.addNum(5)
    test(mf.findMedian(),3)

# Accepted
# 21/21 cases passed (608 ms)
# Your runtime beats 50.86 % of python3 submissions
# Your memory usage beats 75.27 % of python3 submissions (35.8 MB)
