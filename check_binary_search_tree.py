# leetcode 98, 验证二叉搜索树,递归加回溯,维护上下界就可以,或者中序遍历每次和前一个元素比较大小
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#     5
#    / \
#   1   4
#      / \
#     3   6
#
#     5
#    / \
#   1   4
#      /
#     3
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid_bst(root):  # 不允许传入None，最小传入叶子节点
            if not root.left and not root.right:
                return True, root.val, root.val
            condition_left, max_left, min_left = valid_bst(root.left) if root.left else (
            True, -float('inf'), root.val)  # 一定要打括号
            condition_right, max_right, min_right = valid_bst(root.right) if root.right else (
            True, root.val, float('inf'))
            return condition_left and condition_right and max_left < root.val < min_right, max_right, min_left

        def create_tree_from_list(i, arr):
            if i < len(arr) and arr[i]:
                root = TreeNode(arr[i])
                root.left = create_tree_from_list(2 * i + 1, arr)
                root.right = create_tree_from_list(2 * i + 2, arr)
                return root
            else:
                return None

        # root = create_tree_from_list(0,[4,3,6])
        # root = create_tree_from_list(0,[5,1,4,None,None,3,6])
        return valid_bst(root)[0]

# 标答还是厉害一些，递归检查上界下界，或中序遍历每次与前一个比较
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
#             if not node:
#                 return True

#             val = node.val
#             if val <= lower or val >= upper:
#                 return False

#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False
#             return True

#         return helper(root)