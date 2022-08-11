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

        def reverse(head,k):
            dummy = ListNode(None)
            dummy.next = head
            i = 1
            while i < k and head.next: # k个一组意味着挪动k-1次，i from 1 to k-1执行挪动，最后定格在 k
                nxt = head.next
                head.next = nxt.next
                nxt.next = dummy.next
                dummy.next = nxt
                i+=1
            if i == k and head.next: # 如果该组正常完成（即进行了k-1次挪动）且后面还有节点
                head.next = reverse(head.next,k)
            elif i == k: # 如果该组正常完成（即进行了k-1次挪动）且后面没有节点
                pass
            else: # 非正常完成
                head = dummy.next
                for j in range(i-1): # i-1表示挪动的次数
                    nxt = head.next
                    head.next = nxt.next
                    nxt.next = dummy.next
                    dummy.next = nxt
            return dummy.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k(head_node, k):
            if not head_node or not head_node.next or k <= 1:
                return head_node
            
            dummy = ListNode(next=head_node)
            temp, left, right, start, end = head_node, head_node, head_node, dummy, head_node
            while end:
                count = 0
                while count < k:
                    if end:
                        end = end.next
                        count += 1
                    else:
                        break
                if count != k:
                    break
                right = right.next
                #s->1(l)->2(r)->3->e
                while right != end: 
                    temp = right.next
                    right.next = left 
                    left = right
                    right = temp
                #s->1<->2<-3(l) e(r)
                temp = start.next 
                temp.next = end
                # s->1  and 3(l)->2->1(temp)->e(r)
                start.next = left
                # s->3(l)->2->1->e(r)
                start = temp
                temp, left, right, = end, end, end
                # 3->2->1(s)->e(l,r)
            return dummy.next
        return reverse_k(head, k)
