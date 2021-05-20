# NC93 LRU 模拟题, 双向链表, 感觉模拟题最好用面向对象写
class link_node:
    def __init__(self):
        self.next = None
        self.pre = None

class link_list:
    def __init__(self):
        self.head = link_node()
        self.tail = link_node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_first(self, node): #要求node已在链表中
        node.pre.next, node.next.pre = node.next, node.pre
        self.head.next.pre, self.head.next, node.pre, node.next = node, node, self.head, self.head.next

    def insert(self, node): #要求node不在链表中
        self.head.next.pre, self.head.next, node.pre, node.next = node, node, self.head, self.head.next

    def pop_tail(self):
        node = self.tail.pre
        node.pre.next, self.tail.pre = self.tail, node.pre
        return node

class lru:
    def __init__(self, capacity):
        self.key2value = {}
        self.key2node = {}
        self.node2key = {}
        self.link = link_list()
        self.capacity = capacity

    def set(self, key, value):
        if key not in self.key2value:
            self.key2value[key] = value
            node = link_node()
            self.key2node[key] = node
            self.node2key[node] =key
            self.link.insert(node)
            if len(self.key2value) > self.capacity:
                node = self.link.pop_tail()
                key = self.node2key[node]
                self.key2value.pop(key)
                self.key2node.pop(key)
                self.node2key.pop(node)
        else:
            self.key2value[key] = value
            node = self.key2node[key]
            self.link.move_to_first(node)

    def get(self, key):
        if key in self.key2value:
            self.link.move_to_first(self.key2node[key])
            return self.key2value[key]
        else:
            return -1

def LRU(operators, k):
    result = []
    llru = lru(k)
    for operation in operators:
        op = operation[0]
        if op == 1:
            llru.set(operation[1], operation[2])
        else:
            result.append(llru.get(operation[1]))
    return result

if __name__== '__main__':
    result = LRU([[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]], 3)
    pass