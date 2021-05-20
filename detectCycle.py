# 牛客网NC3, 找到链表中环的入口, 快慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head): # 想不到快慢指针就用python集合把之前走过的路径存起来
    if not head or not head.next:
        return None
    fast_node = head
    slow_node = head
    while fast_node != None and fast_node.next != None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
        if fast_node == slow_node:
            fast_node = head
            while(fast_node != slow_node):
                fast_node = fast_node.next
                slow_node = slow_node.next
            return fast_node
    return None