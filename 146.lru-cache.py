#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from utils import test146
# @lc code=start
class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next:ListNode = next
        self.prev:ListNode = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.map: return -1
        node: ListNode = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node:ListNode = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = ListNode(key, value)
            if len(self.map)>=self.capacity:
                n:ListNode = self.tail.prev
                self.map.pop(n.key)
                n.prev.next = self.tail
                self.tail.prev = n.prev
        self.map[key] = node
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
if __name__ == "__main__":
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)
    # lRUCache.put(2, 2)
    # print(lRUCache.get(1))
    # lRUCache.put(3, 3)
    # print(lRUCache.get(2))
    # lRUCache.put(4, 4)
    # print(lRUCache.get(1))
    # print(lRUCache.get(3))
    # print(lRUCache.get(4))

    # lRUCache = LRUCache(2)  #8
    # lRUCache.put(2,1)
    # lRUCache.put(2,2)
    # print(lRUCache.get(2))
    # lRUCache.put(1,1)
    # lRUCache.put(4,1)
    # print(lRUCache.get(2))
    # [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

    # lRUCache = LRUCache(2)  #14
    # lRUCache.put(2,1)
    # lRUCache.put(1,1)
    # lRUCache.put(2,3)
    # lRUCache.put(4,1)
    # print(lRUCache.get(1))
    # print(lRUCache.get(2))
    # [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

    op = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    value = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    test146(LRUCache,op, value)

# Accepted
# 22/22 cases passed (876 ms)
# Your runtime beats 69.65 % of python3 submissions
# Your memory usage beats 10.03 % of python3 submissions (76.5 MB)
