#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
from collections import defaultdict
# @lc code=start
class WordDictionary:

    def __init__(self):
        self.map = [False, dict()]
        

    def addWord(self, word: str) -> None:
        map = self.map
        for char in word:
            if char not in map[1]:
                map[1][char] = [False, dict()]
            map = map[1][char]
        map[0] = True

    def search(self, word: str) -> bool:
        return self.search2(word, 0, self.map)
    
    def search2(self, word, start, map) -> bool:
        while start<len(word) and word[start]!='.':
            if word[start] not in map[1]:
                return False
            map = map[1][word[start]]
            start+=1
        if start == len(word):
            return map[0]
        for key, value in map[1].items():
            if self.search2(word, start+1, value):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
from utils import test
if __name__ == "__main__":
    words = WordDictionary()
    words.addWord("bad")
    words.addWord("dad")
    words.addWord("mad")
    words.addWord("bad")
    test(words.search("pad"), False)
    test(words.search("bad"), True)
    test(words.search(".ad"), True)
    test(words.search("b.."), True)
    words.addWord("pad")
    test(words.search("pad"), True)
    words = WordDictionary() # 11
    words.addWord("at")
    words.addWord("add")
    words.addWord("an")
    words.addWord("and")
    test(words.search("a"), False)


# Accepted
# 13/13 cases passed (296 ms)
# Your runtime beats 83.33 % of python3 submissions
# Your memory usage beats 59.28 % of python3 submissions (27.3 MB)
