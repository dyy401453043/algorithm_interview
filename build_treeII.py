# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# leetcode 106, 从中序和后序获得树，递归11行解决
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hash_table = {val:index for index, val in enumerate(inorder)}
        def build_tree(left, right):
            if left > right:
                return None
            val = postorder.pop()
            idx = hash_table[val]
            node =  TreeNode(val)
            node.right = build_tree(idx+1, right)
            node.left = build_tree(left, idx-1)
            return node
        return build_tree(0, len(inorder)-1)
