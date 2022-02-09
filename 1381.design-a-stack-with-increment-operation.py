#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None]*maxSize
        self.index = 0
        self.maxSize = maxSize
        self.incrementMap = dict()

    def push(self, x: int) -> None:
        if self.index<self.maxSize:
            self.stack[self.index] = x
            self.index += 1

    def pop(self) -> int:
        if self.index == 0: return -1
        self.index -= 1
        addOn = 0
        if self.index in self.incrementMap:
            addOn = self.incrementMap.pop(self.index)
            if self.index>0:
                self.incrementMap[self.index-1]=self.incrementMap.get(self.index-1,0)+addOn
        return self.stack[self.index]+addOn

    def increment(self, k: int, val: int) -> None:
        end = min(k-1, self.index-1)
        if end>=0:
            self.incrementMap[end]=self.incrementMap.get(end, 0)+val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
from utils import test
if __name__ == "__main__":
    cs = CustomStack(3)
    cs.push(1)
    cs.push(2)
    test(cs.pop(), 2)
    cs.push(2)
    cs.push(3)
    cs.push(4)
    cs.increment(5, 100)
    cs.increment(2, 100)
    test(cs.pop(), 103)
    test(cs.pop(), 202)
    test(cs.pop(), 201)
    test(cs.pop(), -1)

    cs = CustomStack(1)
    test(cs.pop(), -1)
    cs.push(1)
    cs.push(2)
    test(cs.pop(), 1)
    cs.push(1)
    cs.increment(5, 100)
    test(cs.pop(), 101)
    test(cs.pop(), -1)
    cs.push(2)
    cs.increment(1, 200)
    test(cs.pop(), 202)
    test(cs.pop(), -1)

    # 21
    cs = CustomStack(2)
    cs.push(34)
    test(cs.pop(), 34)
    cs.increment(8, 100)
    test(cs.pop(), -1)
    cs.increment(9, 91)
    cs.push(63)
    test(cs.pop(), 63)

# Accepted
# 34/34 cases passed (164 ms)
# Your runtime beats 43.49 % of python3 submissions
# Your memory usage beats 69.7 % of python3 submissions (14.9 MB)
