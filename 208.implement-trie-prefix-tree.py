#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.map = [False, dict()]

    def insert(self, word: str) -> None:
        mapp = self.map
        l = len(word)
        for i in range(l):
            if word[i] not in mapp[1]:
                mapp[1][word[i]] = [False, dict()]
            mapp = mapp[1][word[i]]
        mapp[0] = True
        
    def search(self, word: str) -> bool:
        mapp = self.map
        for char in word:
            if char not in mapp[1]:
                return False
            mapp = mapp[1][char]
        return mapp[0]
            
        
    def startsWith(self, prefix: str) -> bool:
        mapp = self.map
        for char in prefix:
            if char not in mapp[1]:
                return False
            mapp = mapp[1][char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
from utils import test
if __name__ == "__main__":
    trie = Trie()
    test(trie.search("a"), False)
    test(trie.startsWith("a"), False)
    trie.insert("apple")
    test(trie.search("app"), False)
    test(trie.startsWith("app"), True)
    test(trie.search("apple"), True)
    trie.insert("app")
    test(trie.startsWith("app"), True)
    test(trie.search("app"), True)

# Accepted
# 15/15 cases passed (152 ms)
# Your runtime beats 84 % of python3 submissions
# Your memory usage beats 71.65 % of python3 submissions (30.3 MB)
