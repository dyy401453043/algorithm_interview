# leetcode 684 生成树，找到第一条冗余边，并查集
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def union(i, j):    # 并
            parent[find(i)] = find(j)

        def find(i):    # 查
            if parent[i] != i:
                parent[i] = find(parent[i])
                return parent[i]
            else:
                return i
        
        for edge in edges:  # 集
            i,j = edge[0],edge[1]
            if find(i) != find(j):
                union(i,j)
            else:
                return edge
