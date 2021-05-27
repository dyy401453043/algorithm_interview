# leetcode 25, K个一组翻转列表，最后小于K个不翻转，穿针引线+递归结合
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def create_linklist(i, arr):
            if i < len(arr):
                node = ListNode(arr[i])
                node.next = create_linklist(i + 1, arr)
                return node
            else:
                return None

        def print_linklink(root):
            while root:
                print(str(root.val) + ' ', end='')
                root = root.next

        def reverse(head, k):
            dummy = ListNode(next=head)
            i = 0
            while i < k - 1 and head.next:  # 穿针引线法，head不主动移动，把nxt提取到dummy后面
                nxt = head.next
                head.next = nxt.next
                nxt.next = dummy.next
                dummy.next = nxt
                i += 1
            if head.next:
                head.next = reverse(head.next, k)
            elif not head.next and i < k - 1:  # 最后一轮要转回来，有点麻烦，在预期之外，强行再转一下吧
                head = dummy.next
                while head.next:
                    nxt = head.next
                    head.next = nxt.next
                    nxt.next = dummy.next
                    dummy.next = nxt
            return dummy.next

        # root = create_linklist(0,[1,2,3,4,5])
        # print_linklink(reverse(root, k=3))
        return reverse(head, k)