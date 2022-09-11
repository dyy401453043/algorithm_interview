# leetcode 332, 用dfs求欧拉通路，挺简洁的
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        adj = defaultdict(list)
        for i, ticket in enumerate(tickets):
            s, t = ticket[0], ticket[1]
            adj[s].append((t, i))
        
        for s in adj.keys():
            adj[s].sort()

        vis = set()
        res = None
        def dfs(src, path):
            nonlocal res
            if res:
                return
            if len(vis) == len(tickets):
                res = path
                return
            for tgt, idx in adj[src]:
                if idx in vis:
                    continue
                else:
                    vis.add(idx)
                    dfs(tgt,path+[tgt])
                    vis.remove(idx)
        dfs('JFK', ['JFK'])
        return res
