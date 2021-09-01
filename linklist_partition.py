class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(val=0, next=head)
        count = 0
        while head.next:
            head = head.next
            count += 1
        tail = head
        pre = dummy
        head = dummy.next
        while count != -1:
            if head.val >= x and tail != head:
                pre.next = head.next
                head.next = None
                tail.next = head
                tail = head
                head = pre.next
            else:
                pre = head
                head = head.next
            count -= 1
        return dummy.next
