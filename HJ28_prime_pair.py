# 华为机试第二十八题，素数伴侣，素数筛加二分图匹配算法
import sys

n = int(input().strip())
nums = [int(i) for i in input().strip().split(' ')]

prime = [True] * 60000
for i in range(2, 246):
    for j in range(i, 60000//i+1):
        if i*j < 60000:
            prime[i*j] = False


flag = [False] * n
odds, evens = [], []
graph = [[False]*n for i in range(n)]
for i in range(n):
    if nums[i] & 1:
        odds.append(i)
    else:
        evens.append(i)
    for j in range(i+1, n):
        if prime[nums[i]+nums[j]]:
            graph[i][j] = True
            graph[j][i] = True

pre = [-1] * n
def dfs(node1, seen):
    for node2 in range(n):
        if graph[node1][node2] and not seen[node2]:
            seen[node2]=True
            if pre[node2] == -1 or dfs(pre[node2], seen):
                pre[node2] = node1
                return True
    return False

for node in odds:
    dfs(node, [False]*n)

# print(odds, evens, pre)
print(sum(1 if pre[i]!=-1 else 0 for i in range(len(pre))))
