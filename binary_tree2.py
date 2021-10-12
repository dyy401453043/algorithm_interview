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

# leetcode 103，锯齿遍历二叉树，队列取出size个元素就能知第几层
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        flag = True
        while len(queue) > 0:
            temp = queue
            queue = []
            for node in temp:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            val_list = [node.val for node in temp]
            result.append(val_list if flag else val_list[::-1])
            flag = not flag
        return result 

if __name__ == '__main__':
    pass
