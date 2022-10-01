# leetcode 399 带权并查集，延时更新
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        f = {}
        w = {}

        for pair in equations:
            a, b  = pair[0], pair[1]
            f[a], w[a] = a, 1
            f[b], w[b] = b, 1
        
        def father(a):
            if a not in f:
                return None
            if f[a] != a:
                final_f = father(f[a])
                w[a] *= w[f[a]]
                f[a] = final_f
            return f[a]
                
        def merge(a, b, v):
            father_a = father(a)
            father_b = father(b)
            f[father_a] = father_b
            w[father_a] = v * w[b] / w[a]

        for pair, v in zip(equations, values):
            a, b  = pair[0], pair[1]
            merge(a, b, v)
        print(f, w)
        
        res = []
        for query in queries:
            a, b  = query[0], query[1]
            father_a = father(a)
            father_b = father(b)
            if father_a and father_b and father_a == father_b:
                res.append(w[a]/w[b])
            else:
                res.append(-1)
        return res
