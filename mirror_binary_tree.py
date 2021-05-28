# 剑指offer 27 镜像二叉树，递归即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def mirror(root):
            if not root:
                return
            mirror(root.left)
            mirror(root.right)
            root.left,root.right = root.right,root.left
            return root
        
        def create_from_list(i,arr):
            if i < len(arr) and arr[i]:
                node = TreeNode(arr[i])
                node.left = create_from_list(2*i+1,arr)
                node.right = create_from_list(2*i+2,arr)
                return node
            else:
                return None

        #return mirror(create_from_list(0,[4,2,7,1,3,6,9]))
        return mirror(root)
