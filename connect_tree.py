"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# leetcode 117, 链表与树综合题，迭代法，挺巧妙
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost:
            head = leftmost
            # dummy 起到了两个效果，1.作为遍历初始值 2.记忆了下一行的首个元素
            pre = dummy = Node() 
            while head:
                if head.left:
                    pre.next = head.left
                    pre = head.left
                if head.right:
                    pre.next = head.right
                    pre = head.right
                head = head.next
            leftmost = dummy.next
        return root
