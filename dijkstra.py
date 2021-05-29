# leetcode 743 图的迪杰斯特拉算法，多复习这个题，有点难记，不优化和堆优化版本
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
    
        # 保存距离和可见信息，2选1
        # distance = {u:float('inf') for u in range(1, n+1)}
        # distance[k] = 0
        # seen = [False] * (n+1) # 下标是节点的值，0不用,第一次循环用k来激发周围节点

        # 或者距离和可见都由最小堆维护, priority_queue
        pq = [(0,k)]
        distance = {}
        # while True:
        #     candidate = -1
        #     distance_cand = float('inf')
        #     for node, dis_cur in distance.items():
        #         if not seen[node] and dis_cur < distance_cand:
        #             candidate = node
        #             distance_cand = dis_cur         
        #     if candidate != -1:
        #         seen[candidate] = True
        #         distance[candidate] = distance_cand
        #         for neighbor, direct_dist in graph[candidate]:
        #             if not seen[neighbor]:
        #                 distance[neighbor] = min(distance[neighbor], distance_cand + direct_dist)
        #     else:
        #         break
        while len(pq) > 0 and len(distance) < n: # pq中会有很多废边
            dis,cand = heapq.heappop(pq)
            if cand not in distance:
                distance[cand] = dis
                for neighbor, direct_dis in graph[cand]:
                    heapq.heappush(pq,(dis+direct_dis,neighbor))
            else:
                continue
        # ans = max(distance.values())
        # return ans if ans < float('inf') else -1
        if len(distance) < n:
            return -1
        else:
            return max(distance.values())
