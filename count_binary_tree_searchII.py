# leetcode95 给定节点数量，输出不同的二叉搜索树列表，递归
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        def get_tree_list(start, end): # 左闭右开
            if start == end:
                return []
            elif start == end - 1:
                return [TreeNode(start)]
            else:
                result = []
                for root_value in range(start,end):
                    left_list = get_tree_list(start,root_value)
                    left_list = left_list if len(left_list) > 0 else [None]
                    right_list = get_tree_list(root_value+1,end)
                    right_list = right_list if len(right_list) > 0 else [None]
                    for left in left_list:
                        for right in right_list:
                            root = TreeNode(root_value)
                            root.left,root.right = left,right
                            result.append(root)
                return result
        return get_tree_list(1, n+1)
