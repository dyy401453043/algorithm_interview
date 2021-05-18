# -*- coding:utf-8 -*-
# 牛客网NC78 反转链表，O(n)，平凡解法
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        stack = []
        if not pHead:
            return None
        while pHead:
            stack.append(pHead)
            pHead = pHead.next
        new_head = stack.pop()
        result = new_head
        while(len(stack) > 0):
            temp = stack.pop()
            new_head.next = temp
            new_head = temp
        new_head.next = None
        return result