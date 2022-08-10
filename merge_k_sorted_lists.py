# leetcode23 合并k个有序数组，动手实现最小堆
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_from_list(arr):
    if len(arr) == 0:
        return None
    head = LinkNode(arr[0])
    pre = head
    for i in range(1, len(arr)):
        node = LinkNode(arr[i])
        pre.next = node
        pre = node
    return head

class MinHeap:
    def __init__(self, node_list):
        self.arr = [node for node in node_list]
        self.length = len(self.arr)
        for i in range(self.length-1, -1, -1): # build head, time O(klogk)
            self.drop(i)

    def drop(self, idx):
        minidx = idx
        l, r = 2*idx+1, 2*idx+2
        if l < self.length and self.arr[l].val < self.arr[minidx].val:
            minidx = l
        if r < self.length and self.arr[r].val < self.arr[minidx].val:
            minidx = r
        if minidx != idx:
            self.arr[idx], self.arr[minidx] = self.arr[minidx], self.arr[idx]
            self.drop(minidx)
    
    def get_min(self): # call ensure sel.length > 0
        min_node = self.arr[0]
        if min_node.next:
            next_node = min_node.next
            self.arr[0] = next_node
            self.drop(0)
        else:
            self.arr[0], self.arr[self.length-1] = self.arr[self.length-1], self.arr[0]
            self.length -= 1
            self.drop(0)
        return min_node.val

if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    head_list = [build_from_list(list_i) for list_i in lists]
    min_heap = MinHeap(head_list)

    result = []
    while min_heap.length > 0:
        result.append(min_heap.get_min())

    print(result)
