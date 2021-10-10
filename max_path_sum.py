# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# leetcode 124, 找到二叉树中的最大路径和，思路有点小难度，递归。
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = -float('inf')
        def max_gain(node): # ensure node is not None
            nonlocal max_path
            if not node.left and not node.right:
                if node.val > max_path:
                    max_path = node.val
                return node.val
            left_gain, right_gain = 0, 0
            if node.left:
                temp = max_gain(node.left)
                if temp > left_gain:
                    left_gain = temp
            if node.right:
                temp = max_gain(node.right)
                if temp > right_gain:
                    right_gain = temp
            if left_gain + right_gain + node.val > max_path:
                max_path = left_gain + right_gain + node.val
            return max(left_gain, right_gain) + node.val
        max_gain(root)
        return max_path
