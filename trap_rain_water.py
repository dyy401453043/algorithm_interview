# leetcode 407 二维接雨水，最小堆，每个点接水一次，最小的已接水点给周围未接水点加水
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        seen = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    seen[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j],i,j))

        res = 0
        directions = [-1,0,1,0,-1]
        while heap:
            height, i, j = heapq.heappop(heap)
            for k in range(4):
                temp_i, temp_j = i + directions[k], j + directions[k+1]
                if 0<=temp_i<m and 0<=temp_j<n and not seen[temp_i][temp_j]:
                    if height > heightMap[temp_i][temp_j]:
                        res += height - heightMap[temp_i][temp_j]
                    seen[temp_i][temp_j] = True
                    heapq.heappush(heap, (max(heightMap[temp_i][temp_j], height), temp_i, temp_j))
        return res
