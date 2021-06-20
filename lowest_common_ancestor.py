# 牛客网 NC102 找两个节点的最近公共祖先 标答有点简洁
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        # write_first, my first idea
#         in_tree_list = [] 
#         def in_tree(root,val1,val2):
#             result = [False, False]
#             result1,result2 = [False, False],[False, False]
#             if root.left:
#                 result1 = in_tree(root.left,val1,val2)
#             if root.right:
#                 result2 = in_tree(root.right,val1,val2)
#             result[0] = result1[0] or result2[0] or root.val == val1
#             result[1] = result1[1] or result2[1] or root.val == val2
#             if result[0] and result[1]:
#                 in_tree_list.append(root.val)
#             return result
#         in_tree(root, o1, o2)
#         return in_tree_list[0]
        # write_second
        def last_search(root,val1,val2):
            if root.val == val1 or root.val == val2:
                return root
            left,right = None,None
            if root.left:
                left = last_search(root.left, val1, val2)
            if root.right:
                right = last_search(root.right, val1, val2)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return last_search(root,o1,o2).val
