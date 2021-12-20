#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
BOTH_NONE = 0
LEFT_DONE = 1
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result =list()
        stack = [root]
        while stack:
            node = stack.pop()
            if node!=None:
                result.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                result.append('N')
        return '.'.join(result)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_list = data.split('.')
        sentinel = TreeNode()
        stack = [[sentinel, BOTH_NONE]]
        for i, node in enumerate(tree_list):
            if node[0]=='N':
                node = None
            else:
                node = TreeNode(int(node))
            if stack[-1][1]==BOTH_NONE:
                stack[-1][0].left = node
                stack[-1][1] += 1
                if node!=None:
                    stack.append([node, BOTH_NONE])
            else:
                stack[-1][0].right = node
                stack.pop()
                if node!=None:
                    stack.append([node, BOTH_NONE])
        return sentinel.left



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
from utils import test, list2TreeNode, treeNode2List
if __name__ == "__main__":
    codec = Codec()
    tree_list = [1,2,3,None,None,4,5]
    tree = list2TreeNode(tree_list)
    s = codec.serialize(tree)
    test(s, "1.2.N.N.3.4.N.N.5.N.N")
    ds = codec.deserialize(s)
    new_tree_list = treeNode2List(ds)
    test(new_tree_list, tree_list)

    tree_list = []
    tree = list2TreeNode(tree_list)
    s = codec.serialize(tree)
    test(s, "N")
    ds = codec.deserialize(s)
    new_tree_list = treeNode2List(ds)
    test(new_tree_list, tree_list)

    tree_list = [1]
    tree = list2TreeNode(tree_list)
    s = codec.serialize(tree)
    test(s, "1.N.N")
    ds = codec.deserialize(s)
    new_tree_list = treeNode2List(ds)
    test(new_tree_list, tree_list)

# Accepted
# 52/52 cases passed (124 ms)
# Your runtime beats 61.2 % of python3 submissions
# Your memory usage beats 83.61 % of python3 submissions (18.8 MB)
