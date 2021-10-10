# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# leetcode 82, 删除排序链表中的重复元素，全删除，双指针加标识位
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        duplicate = False
        while cur: # pre永不陷入泥潭，cur可以陷入泥潭
            nxt = cur.next
            if not nxt:
                break
            if cur.val == nxt.val:
                duplicate = True
                pre.next = nxt
                cur = nxt
            else:
                if duplicate: # cur能走出泥潭，但是cur已经沾染污泥，所以卸磨杀驴
                    pre.next = nxt
                    cur = nxt
                    duplicate = False
                else:
                    pre = cur
                    cur = nxt
        if duplicate: # cur到最后都没走出泥潭
            pre.next = None
        return dummy.next
