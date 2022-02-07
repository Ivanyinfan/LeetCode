#
# @lc app=leetcode id=536 lang=python3
#
# [536] Construct Binary Tree from String
#
from typing import Optional
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
BOTH_PENDING = 2
LEFT_DONE = 1
BOTH_DONE = 0
class Solution:
    def BackStep(self, stack):
        node = stack.pop()[0]
        if stack[-1][1] == BOTH_PENDING:
            stack[-1][0].left = node
        elif stack[-1][1] == LEFT_DONE:
            stack[-1][0].right = node
        stack[-1][1] -= 1

    def str2tree(self, s: str) -> Optional[TreeNode]:
        current = None
        stack = list()
        number = None
        negative = False
        for i, char in enumerate(s):
            # stack_val = list(map(lambda x:x[0].val, stack))
            if char.isdigit():
                if number == None: number = 0
                number = number*10 + int(char)
            elif char == '-':
                negative = True
            elif char == '(':
                if number == None:
                    pass
                else:
                    if negative: number = - number
                    current = TreeNode(number)
                    stack.append([current, BOTH_PENDING])
                    number = None
                    negative = False
            else:
                if number != None:
                    if negative: number = - number
                    stack.append([TreeNode(number), BOTH_DONE])
                self.BackStep(stack)
                number = None
                negative = False
        if not stack:
            if not number: return None
            if negative: number = - number
            return TreeNode(number)
        return stack[0][0]
# @lc code=end
from utils import test, treeNode2List
if __name__ == "__main__":
    sol = Solution()
    test(treeNode2List(sol.str2tree("4(2(3)(1))(6(5))")),[4,2,6,3,1,5])
    test(treeNode2List(sol.str2tree("4(2(3)(1))(6(5)(7))")), [4,2,6,3,1,5,7])
    test(treeNode2List(sol.str2tree("-4(2(3)(1))(6(5)(7))")), [-4,2,6,3,1,5,7])
    test(treeNode2List(sol.str2tree("-4")), [-4])
    test(treeNode2List(sol.str2tree("-4(2)(-3)")), [-4,2,-3])

# 执行结果：通过
# 显示详情
# 添加备注

# 执行用时：88 ms, 在所有 Python3 提交中击败了37.59%的用户
# 内存消耗：16 MB, 在所有 Python3 提交中击败了9.02%的用户
# 通过测试用例：86 / 86
