# 剑指offer 26 判断树B是不是树A的子结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recur(A, B): #以A为根的树是否同根包含子树B
    if not B: return True
    if not A: return False
    if A.val != B.val: return False
    return recur(A.left, B.left) and recur(A.right, B.right)

def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
