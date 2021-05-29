# leetcode 133, 图克隆，visited可作映射使用自己写的时候没有想到
# 图的遍历，入队（栈）前标记节点已访问，出队（栈）时执行动作，然后邻居入队（栈）[入队（栈）之前检查邻居是否已经访问]
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 连通图
#   1
#2      4
#   3
# import copy

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def build_graph(adjList):
            node_list = [Node(i+1) for i in range(len(adjList))]
            for i,adj in enumerate(adjList):
                node_list[i].neighbors = [node_list[j-1] for j in adj]
            return node_list[0]
        
        def print_graph(node):
            visited = set()
            stack = []
            visited.add(node)
            stack.append(node)
            while len(stack) > 0:
                node = stack.pop()
                print(str(node.val)+' ',end='')
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        # node = build_graph([[2,4],[1,3],[2,4],[1,3]])
        if not node:
            return node         
        bfs_queue = []
        visited = {} # 用字典当visited，不仅有检查是否曾经访问的功能，还能形成原节点到克隆节点的映射
        bfs_queue = [node] + bfs_queue 
        visited[node] = Node(node.val,[]) # 入队时创建节点并标记已访问，出队时先添加邻居（不检查访问），然后邻居入队（检查访问）
        while len(bfs_queue) > 0:
            cur_node = bfs_queue.pop()
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val,[])
                    bfs_queue = [neighbor] + bfs_queue
                visited[cur_node].neighbors.append(visited[neighbor])
        return visited[node]
