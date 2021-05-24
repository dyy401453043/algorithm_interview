# leetcode 2, 两数相加链表版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        head.next = l3 = ListNode(0)
        carry = False
        while l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            value = value1 + value2
            carry = l3.val+value>=10
            l1,l2 = l1.next if l1 else None, l2.next if l2 else None
            if carry:
                l3.val += value-10
                l3.next = ListNode(1)
            else:
                l3.val += value
                if l1 or l2:
                    l3.next = ListNode(0)
            l3 = l3.next
        return head.next
