#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def get_lr_remove(self, s):
        count = rRemove = 0
        for char in s:
            if char=='(': count+=1
            elif char==')': count-=1
            if count<0: count, rRemove = 0, rRemove+1
        return count, rRemove

    def backtrack(self, s, index, left_count, right_count, lRemove, rRemove, path:list, result:set):
        if index==len(s):
            if lRemove==0 and rRemove==0:
                result.add(''.join(path))
            return
        if lRemove+rRemove>len(s)-index:
            return
        if s[index]=='(':
            path.append(s[index])
            self.backtrack(s,index+1,left_count+1,right_count,lRemove,rRemove,path,result)
            path.pop()
            self.backtrack(s,index+1,left_count,right_count,lRemove-1,rRemove,path,result)
        elif s[index]==')':
            if left_count>right_count:
                path.append(s[index])
                self.backtrack(s,index+1,left_count,right_count+1,lRemove,rRemove,path,result)
                path.pop()
            self.backtrack(s,index+1,left_count,right_count,lRemove,rRemove-1,path,result)
        else:
            path.append(s[index])
            self.backtrack(s,index+1,left_count,right_count,lRemove,rRemove,path,result)
            path.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        lRemove, rRemove = self.get_lr_remove(s)
        result = set()
        self.backtrack(s,0,0,0,lRemove,rRemove,list(),result)
        return list(result)
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.removeInvalidParentheses("()())()"),["(())()","()()()"],False)
    test(sol.removeInvalidParentheses("(a)())()"),["(a())()","(a)()()"],False)
    test(sol.removeInvalidParentheses(")("),[""],False)
    test(sol.removeInvalidParentheses("("),[""],False)
    test(sol.removeInvalidParentheses(")"),[""],False)
    test(sol.removeInvalidParentheses("(()()((()())"),["()()(()())","()()((()))","(())(()())","(())((()))","(()()()())","(()()(()))"],False)
    test(sol.removeInvalidParentheses("(((()"),["()"],False)

# Accepted
# 127/127 cases passed (1320 ms)
# Your runtime beats 43.34 % of python3 submissions
# Your memory usage beats 75.2 % of python3 submissions (14.4 MB)
