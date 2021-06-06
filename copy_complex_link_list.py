# leetcode 剑指offer 35 拷贝复杂链表
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node2node = {}
        dummy = pre = Node(0)
        cur = head
        while cur: # 一次循环，拷贝链表的逻辑
            node = Node(cur.val)
            pre.next = node
            node2node[cur] = node
            cur = cur.next
            pre = node
        cur = head
        while cur:  # 在所有节点都被创建后再进行遍历，链接random字段
            node = node2node[cur]
            if cur.random:
                node.random = node2node[cur.random]
            cur = cur.next
        return dummy.next
