# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# leetcode 109，从中序链表中去建树，技巧
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        def build_tree(left, right):
            if left > right:
                return None
            mid = int((left + right)/2)
            root = TreeNode()
            root.left = build_tree(left, mid-1)
            nonlocal head
            # 这两步非常巧妙，用中序遍历序列按中序遍历去建树，降低时间复杂度
            root.val = head.val
            head = head.next
            root.right = build_tree(mid+1, right)
            return root
        
        return build_tree(0, get_length(head)-1)
