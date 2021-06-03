# leetcode 547 寻找联通分量数量，并查集
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        def union(i,j):
            parent[find(i)] =  find(j)
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
                return parent[i]
            else:
                return i

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]==1:
                    if find(i) != find(j):
                        union(i,j)
        
        # result = set()
        # for i in range(n):
        #     if find(i) not in result:
        #         result.add(find(i))
        result = 0
        for i in range(n):
            if parent[i] == i:
                result+=1
        return result
