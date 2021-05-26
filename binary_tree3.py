# leetcode102 二叉树层序遍历,bfs+自写测试样例(完全二叉树)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#       1
#   2       3
#4      5
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def create_complete_tree(x,n):
            if x <= n:
                node = TreeNode(x)
                node.left = create_complete_tree(2*x,n)
                node.right = create_complete_tree(2*x+1,n)
                return node
            else:
                return None

        def bfs(root):
            if root == None:
                return []
            result=[]
            bfs_list = []
            layer_list = []
            bfs_list,layer_list = [root] + bfs_list, [0] + layer_list
            now_layer = - 1
            while(len(bfs_list)>0):
                node,layer = bfs_list.pop(),layer_list.pop()
                if layer > now_layer:
                    result.append([])
                    now_layer = layer
                result[layer].append(node.val)
                if node.left:
                    bfs_list,layer_list = [node.left] + bfs_list, [layer+1] + layer_list
                if node.right:
                    bfs_list,layer_list = [node.right] + bfs_list, [layer+1] + layer_list
            return result

        # root = create_complete_tree(1, 5)
        return bfs(root)