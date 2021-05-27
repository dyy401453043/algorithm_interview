# leetcode 19, 删除倒数第n个节点，快慢指针
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def create_arr(i,arr):
            if i < len(arr):
                root = ListNode(arr[i])
                root.next = create_arr(i+1,arr)
                return root
            else:
                return None
        # head,n = create_arr(0,[1]),1
        dummy = ListNode(next=head)
        fast,slow = dummy,dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next