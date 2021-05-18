# 牛客网NC45，二叉树的中序遍历，迭代版，字节一面

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solution(root):
    result = []
    left_stack = []
    while len(left_stack) > 0 or root:
        left_stack.append(root)
        while root.left is not None:
            root = root.left
            left_stack.append(root)
        root = left_stack.pop()
        result.append(root)
        while root.right is None and len(left_stack) > 0:
            root = left_stack.pop()
            result.append(root)
        if root.right is not None:
            root = root.right
        else:
            break

if __name__ == '__main__':
    pass