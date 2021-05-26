# leetcode 110, 检测平衡二叉树，dfs，维护高度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_dfs(root)->(bool,int):
            if not root:
                return True, 0
            con1, depth_left = check_dfs(root.left)
            con2, depth_right = check_dfs(root.right)
            con3 = abs(depth_left-depth_right) <= 1
            return con1 and con2 and con3, max(depth_left, depth_right) + 1

        def create_tree_from_arr(i, arr):
            if i < len(arr) and arr[i]:
                root = TreeNode(arr[i])
                root.left = create_tree_from_arr(2*i+1, arr)
                root.right = create_tree_from_arr(2*i+2, arr)
                return root
            else:
                return None
        
        # root = create_tree_from_arr(0,[3,9,20,None,None,15,7])
        # print(check_dfs(root))
        return check_dfs(root)[0]
