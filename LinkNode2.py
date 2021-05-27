# leetcode 92 ,指定区域反转链表，穿针引线法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def creat_list_from_arr(i,arr):
            if i < len(arr):
                node = ListNode(arr[i])
                node.next = creat_list_from_arr(i+1, arr)
                return node
            else:
                return None

        def print_linklist(root):
            while root:
                print(str(root.val) + ' ', end='')
                root = root.next
        
        # head = creat_list_from_arr(0,[1,2,3,4,5])
        # left,right = 2,4
        dummy = ListNode(next=head)
        pre = dummy
        for i in range(left-1):
            pre = head
            head = head.next
        # 最后检查一下left==right
        for i in range(right-left): # head不主动移动，把nxt提前到pre之后
            nxt = head.next
            head.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        # print_linklist(dummy.next)
        return dummy.next
        
