#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
from collections import deque
# @lc code=start
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.current = None

    def push(self, x: int) -> None:
        if self.current:
            self.queue.append(self.current)
        self.current = x

    def pop(self) -> int:
        r = self.current
        if len(self.queue)==0:
            self.current = None
        else:
            count = 0
            while count<len(self.queue)-1:
                self.queue.append(self.queue.popleft())
                count += 1
            self.current = self.queue.popleft()
        return r

    def top(self) -> int:
        return self.current

    def empty(self) -> bool:
        return self.current==None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
from utils import test
if __name__ == "__main__":
    myStack = MyStack()
    test(myStack.empty(),True)
    myStack.push(1)
    myStack.push(2)
    test(myStack.top(),2)
    test(myStack.pop(),2)
    test(myStack.empty(),False)
    test(myStack.top(),1)
    test(myStack.pop(),1)
    test(myStack.empty(),True)
    myStack.push(3)
    test(myStack.top(),3)
    test(myStack.pop(),3)
    test(myStack.empty(),True)

# Accepted
# 16/16 cases passed (35 ms)
# Your runtime beats 22.36 % of python3 submissions
# Your memory usage beats 73.96 % of python3 submissions (14.2 MB)
