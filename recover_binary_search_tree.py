# leetcode 99, 二叉搜索树中有两个元素发生了交换，找到他们。注意中序遍历是增序列。
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def mid_search(node): # ensure node is not None
            modify_node1, modify_node2 = None, None
            stack = []
            last_node = TreeNode(val=-float('inf'))
            first = True
            while True:
                while node.left:
                    stack.append(node)
                    node = node.left
                if node.val < last_node.val:
                    if first:
                        modify_node1, modify_node2 = last_node, node
                        first = False
                    else:
                        modify_node2 = node
                last_node = node
                while not node.right and len(stack) > 0:
                    node = stack.pop()
                    if node.val < last_node.val:
                        if first:
                            modify_node1, modify_node2 = last_node, node
                            first = False
                        else:
                            modify_node2 = node
                    last_node = node
                if node.right:
                    node = node.right
                else:
                    break
            assert len(stack) == 0
            return modify_node1, modify_node2
        modify_node1, modify_node2 = mid_search(root)
        modify_node1.val, modify_node2.val = modify_node2.val, modify_node1.val
        return root
