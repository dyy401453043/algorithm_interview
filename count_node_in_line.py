# leetcode 149, 最多共线的点数量，用斜率和最小编号点来表示一条直线
def gcd(a ,b): # 求最大公约数
    if a % b == 0 or b % a == 0:
        return min(a, b)
    double = 0
    while a % 2 == 0 and b % 2 == 0:
        double += 1
        a = a / 2
        b = b / 2
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a * 2 ** double

def get_ration(node1, node2):
    a = node1[0] - node2[0]
    b = node1[1] - node2[1]
    if b == 0:
        return (1,0)
    if a == 0:
        return (0,1)
    negative = False
    if a > 0 and b < 0 or a < 0 and b > 0:
        negative = True
    a, b = abs(a) , abs(b)
    k = gcd(a, b)
    a, b = a/k, b/k
    return (-a, b) if negative else (a, b)
    
def max_node_in_line(points):
    if len(points)==0:
        return 0
    if len(points)==1:
        return 1
    max_line = 2
    ration2node = {} # k+root -> set
    length = len(points)
    for i in range(length):
        skip = set() #不要与共线的点重复计算，剪枝 
        for j in range(i):
            if j in skip:
                continue
            ration = get_ration(points[j], points[i])
            if (ration, j) in ration2node:
                skip.update(ration2node[(ration, j)])
                ration2node[(ration,j)].add(i)
                if len(ration2node[(ration,j)]) > max_line:
                    max_line = len(ration2node[(ration,j)])
            else:
                ration2node[(ration,j)] = set([j, i])
    return max_line

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(max_node_in_line(points))
