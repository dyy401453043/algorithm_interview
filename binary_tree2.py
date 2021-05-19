# 牛客网 NC14，二叉树之自行层序遍历在，就是每一层改变方向，bfs ，高性能通过
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    if not root:
        return []
    result = []
    max_layer = -1
    initial_layer = 0
    queue = []
    layers = []
    queue.append(root)
    layers.append(initial_layer)
    while (len(queue) > 0):
        root, queue = queue[0], queue[1:]
        layer = layers[0]
        layers = layers[1:]
        if layer > max_layer:
            result.append([])
            max_layer = layer
        result[layer] = result[layer] + [root.val] if layer % 2 == 0 else [root.val] + result[layer]
        if root.left:
            queue.append(root.left)
            layers.append(layer + 1)
        if root.right:
            queue.append(root.right)
            layers.append(layer + 1)
    return result

if __name__ == '__main__':
    pass