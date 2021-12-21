#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
from typing import List
# @lc code=start
class Solution:
    def isPalindrome(self, word, end):
        if end<1:
            return True
        start = 0
        while start<end:
            if word[start]!=word[end]:
                return False
            start, end = start+1, end-1
        return True

    def findValidPrefix(self, word):
        r = list()
        l = len(word)
        for i in range(l):
            if self.isPalindrome(word,i):
                r.append(i)
        return r

    def findValidSuffix(self, word):
        L = len(word)
        r = self.findValidPrefix(str(reversed(word)))
        return [L-i-1 for i in r]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_map = dict()
        result = list()
        for i, word in enumerate(words):
            words_map[word]=i
        for i, word in enumerate(words):
            l = len(word)
            if l==0: continue
            prefix = self.findValidPrefix(word)
            suffix = self.findValidSuffix(word)
            for p in prefix:
                target = word[l-1:p:-1]
                index = words_map.get(target,-1)
                if index!=-1 and index!=i:
                    result.append([index, i])
            for s in suffix:
                index = words_map.get(word[0:s:-1], -1)
                if index!=-1 and index!=i:
                    result.append([i, index])
            if suffix[0]!=0:
                index = words_map.get(word[::-1],-1)
                if index!=-1:
                    result.append([i, index])
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.palindromePairs(words=["abcd","dcba","lls","s","sssll"]),answer=[[0,1],[1,0],[3,2],[2,4]],ordered=False)
    test(sol.palindromePairs(words = ["bat","tab","cat"]),answer=[[0,1],[1,0]],ordered=False)
    test(sol.palindromePairs(words = ["a",""]),answer=[[0,1],[1,0]],ordered=False)