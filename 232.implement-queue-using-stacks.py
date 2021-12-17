#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def getStack2(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        self.getStack2()
        return self.stack2.pop()

    def peek(self) -> int:
        self.getStack2()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1)==0 and len(self.stack2)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
from utils import test
if __name__ == "__main__":
    myQueue = MyQueue()
    test(myQueue.empty(),True)
    myQueue.push(1)
    myQueue.push(2)
    test(myQueue.peek(),1)
    test(myQueue.pop(),1)
    test(myQueue.empty(),False)
    myQueue.push(3)
    test(myQueue.pop(),2)
    test(myQueue.pop(),3)
    test(myQueue.empty(),True)

# Accepted
# 21/21 cases passed (35 ms)
# Your runtime beats 22.41 % of python3 submissions
# Your memory usage beats 91.4 % of python3 submissions (14.2 MB)
