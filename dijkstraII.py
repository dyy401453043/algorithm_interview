# leetcode 1786 堆优化dijkstra + 记忆化搜索
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append((edge[1],edge[2]))
            graph[edge[1]].append((edge[0],edge[2]))
        
        visited = [False for i in range(n+1)]
        distance = [float('inf') for i in range(n+1)]
        distance[n] = 0 # n 为源点

        min_heap = [(0,n)]
        
        while len(min_heap) > 0:
            dis_cand, candidate = heapq.heappop(min_heap)
            if visited[candidate]:
                continue

            visited[candidate] = True
            for neighbor, dis_direct in graph[candidate]:
                if dis_cand + dis_direct < distance[neighbor]:
                    distance[neighbor] = dis_cand + dis_direct
                    heapq.heappush(min_heap,(dis_cand + dis_direct,neighbor))
                    # 堆优化改动 13，15，24就可以，其他的是原先的逻辑也是必要

        node_list = [i for i in range(1,n+1)]
        node_list.sort(key = lambda x:distance[x])
        path = collections.defaultdict(int)
        path[n] = 1
        for node in node_list:
            for neighbor,_ in graph[node]:
                if distance[neighbor] > distance[node]:
                    path[neighbor] += path[node]
        return path[1] % (1000000000+7)
