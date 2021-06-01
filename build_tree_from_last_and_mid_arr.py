# 从中序序列和后序序列中将二叉树重建，自写测试样例
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

#           1
#       2      3
#   4     5  6   7
#8   9  10
def create_complete_tree(i, n):
    if i <= n:
        node = TreeNode(i)
        node.left = create_complete_tree(2*i,n)
        node.right = create_complete_tree(2*i+1,n)
        return node
    else:
        return None

def last_search(root):
    result = []
    node_stack = [root]
    while len(node_stack) > 0:
        node = node_stack.pop()
        result.append(node.val)
        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)
    result.reverse()
    return result

def mid_search(root):
    result = []
    node_stack = []
    while True:
        while root.left:
            node_stack.append(root)
            root = root.left
        result.append(root.val)
        while not root.right and len(node_stack) > 0:
            root = node_stack.pop()
            result.append(root.val)
        if root.right:
            root = root.right
        else:
            break
    return result

#[left_tree,root,right_tree]
#[left_tree,right_tree,root]
def build_tree_from_mid_last(arr_mid,l_mid,r_mid,arr_last,l_last,r_last,map_mid,map_last): # require l<=r
    root_value = arr_last[r_last]
    root = TreeNode(root_value)
    left_length = map_mid[root_value] - 1 - l_mid
    if left_length >= 0:
        root.left = build_tree_from_mid_last(arr_mid, l_mid, l_mid+left_length,
                                             arr_last, l_last, l_last+left_length,
                                             map_mid, map_last)
    right_length = r_mid - (map_mid[root_value] + 1)
    if right_length >= 0:
        root.right = build_tree_from_mid_last(arr_mid, r_mid-right_length, r_mid,
                                             arr_last, r_last-1-right_length, r_last-1,
                                             map_mid, map_last)
    return root

def print_tree(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop()
        print(str(node.val)+' ',end='')
        if node.left:
            queue = [node.left]+queue
        if node.right:
            queue = [node.right]+queue

if __name__ == '__main__':
    root = create_complete_tree(1, 10)
    arr_mid = mid_search(root)
    arr_last = last_search(root)
    print("中序：{}".format(arr_mid))
    print("后序：{}".format(arr_last))
    map_mid = [-1] * (len(arr_mid)+1)
    for index, num in enumerate(arr_mid):
        map_mid[num] = index
    map_last = [-1] * (len(arr_mid)+1)
    for index, num in enumerate(arr_last):
        map_last[num] = index
    root = build_tree_from_mid_last(arr_mid, 0, len(arr_mid)-1, arr_last, 0, len(arr_last)-1, map_mid, map_last)
    print("根据中序后序建树，层序打印：")
    print_tree(root)