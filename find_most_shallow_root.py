# leetcode 310，在多叉树中找到树深最浅的根节点，自底向上的bfs，维护节点的度数
import copy
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for edge in edges:
            u,v = edge[0],edge[1]
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        node_list = []
        while len(degree) > 2: # 每轮循环剥离出出度为1的点，到最后剩下的1或者2个点即是本题答案
            nodes = [i for i in degree.keys() if degree[i] == 1]
            node_list.append(nodes)
            for u in nodes:
                for neighbor in graph[u]:
                    if neighbor in degree:
                        degree[neighbor] -= 1
                degree.pop(u)
        return [i for i in degree.keys()]
            
